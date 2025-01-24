import sys
import os
import subprocess
import re
import psutil
import platform
from packaging import version
import requests
from bs4 import BeautifulSoup
from . import pypi


_system = platform.system()


_version_command = """
import torch
print(torch.__version__ + "\\0" + str(torch.version.cuda))
"""
def torch_cuda_version():
    torch_version, cuda_version = subprocess.run([parent_python, "-c", _version_command], capture_output=True, text=True).stdout[:-1].split("\0")
    if cuda_version == 'None':
        cuda_version = None
    return torch_version, cuda_version


def format_cuda_version(cuda_version):
    if cuda_version is None:
        cuda_version_formatted = 'cpu'
    else:
        cuda_version_formatted = f'cu{"".join(cuda_version.split("."))}'
    return cuda_version_formatted


def generate_possible_natten_versions(natten_version, cuda_version_formatted):
    regex_natten_version = natten_version.replace('.', '\.')
    pattern = f'torch([^\s/]+)\/natten-{regex_natten_version}\+torch([^\s/]+){cuda_version_formatted}'
    url = "https://shi-labs.com/natten/wheels/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            content = link.get_text(strip=True)
            if content is not None:
                searched = re.search(pattern, content)
                if searched is not None:
                    yield searched.group(1), searched.group(2)


def find_closest_version_index(version_list, target_version):
    target = version.parse(target_version)
    def version_to_tuple(v):
        v = version.parse(str(v))
        return (v.major, v.minor, v.micro)
    index, _ = min(enumerate(version_list), key=lambda v: sum(abs(a - b) for a, b in zip(version_to_tuple(v[1]), version_to_tuple(target))))
    return index


def make_natten_package_command(natten_version):
    if _system == 'Linux':
        torch_version, cuda_version = torch_cuda_version()
        cuda_version_formatted = format_cuda_version(cuda_version)
        torch_versions, torch_simple_versions = map(list, zip(*generate_possible_natten_versions(natten_version, cuda_version_formatted)))
        torch_version_index = find_closest_version_index(torch_versions, torch_version)
        version_without_cuda = f'{natten_version}+torch{torch_simple_versions[torch_version_index]}'
        complete_natten_version = f'{version_without_cuda}{cuda_version_formatted}'
        command = f'natten=={complete_natten_version} -f https://shi-labs.com/natten/wheels/'
    else:
        command = f'natten=={natten_version}'
    return command


def install_natten(natten_version, executable = sys.executable):
    pypi.install(make_natten_package_command(natten_version), executable)


def parent_python():
    parent_process = psutil.Process(os.getppid())
    return parent_process.exe()