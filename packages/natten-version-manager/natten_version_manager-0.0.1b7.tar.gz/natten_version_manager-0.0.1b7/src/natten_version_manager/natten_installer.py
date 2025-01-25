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


_natten_link = "https://shi-labs.com/natten/wheels/"


def get_smi_cuda_version():
    try:
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            output = result.stdout
            match = re.search(r'CUDA Version\s*:\s*(\d+\.\d+)', output)
            if match:
                return match.group(1)
    except Exception:
        return None


_version_command = """
try:
    import torch
    print(torch.__version__ + "\\0" + str(torch.version.cuda))
except ModuleNotFoundError:
    print("\\0")
"""
def torch_cuda_version(executable = sys.executable):
    process = subprocess.run([executable, '-c', _version_command], capture_output=True, text=True)
    out = process.stdout[:-1]
    if out == '\0':
        torch_version = pypi.get_latest_version('torch')
        cuda_version = get_smi_cuda_version()
    else:
        torch_version, cuda_version = out.split('\0')
        if cuda_version == 'None':
            cuda_version = None
    return torch_version, cuda_version


def format_cuda_version(cuda_version):
    if cuda_version is None:
        cuda_version_formatted = 'cpu'
    else:
        cuda_version_formatted = f'cu{"".join(cuda_version.split("."))}'
    return cuda_version_formatted


def generate_possible_natten_versions(natten_version):
    regex_natten_version = natten_version.replace('.', '\.')
    pattern = f'torch([^\s/]+)\/natten-{regex_natten_version}\+torch([^\s/]+)(cu(\d)+|cpu)-'
    url = _natten_link
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            content = link.get_text(strip=True)
            if content is not None:
                searched = re.search(pattern, content)
                if searched is not None:
                    yield searched.group(1), searched.group(2), searched.group(3), link['href']


def find_closest_version_index(version_list, target_version):
    target = version.parse(target_version)
    def version_to_tuple(v):
        v = version.parse(str(v))
        return (v.major, v.minor, v.micro)
    index, _ = min(enumerate(version_list), key=lambda v: sum(abs(a - b) for a, b in zip(version_to_tuple(v[1]), version_to_tuple(target))))
    return index


if _system == 'Linux':
    def set_find_links(executable = sys.executable):
        find_links = pypi.config_get('find-links', executable=executable)
        if find_links is None or find_links != _natten_link:
            pypi.config_set('find-links', _natten_link, executable=executable)
        return find_links


    def make_natten_package_command(natten_version, executable = sys.executable, is_link_mode = True):
        torch_version, cuda_version = torch_cuda_version(executable)
        cuda_version_formatted = format_cuda_version(cuda_version)
        torch_versions, torch_simple_versions, cuda_simple_versions, links = map(list, zip(*generate_possible_natten_versions(natten_version)))
        if cuda_version_formatted not in cuda_simple_versions:
            cuda_version_formatted = max(cuda_simple_versions)
        torch_versions, torch_simple_versions, links = map(list, zip(*[
            (torch_version, torch_simple_version, link)
            for torch_version, torch_simple_version, cuda_simple_version, link in
            zip(torch_versions, torch_simple_versions, cuda_simple_versions, links) if cuda_simple_version == cuda_version_formatted
        ]))
        torch_version_index = find_closest_version_index(torch_versions, torch_version)
        if is_link_mode:
            return [f'natten @ {_natten_link}{links[torch_version_index]}']
        else:
            version_without_cuda = f'{natten_version}+torch{torch_simple_versions[torch_version_index]}'
            complete_natten_version = f'{version_without_cuda}{cuda_version_formatted}'
            return [f'natten=={complete_natten_version}']


    def unset_find_links(old, executable = sys.executable):
        pypi.config_unset('find-links', executable=executable)
        if old is not None:
            pypi.config_set('find-links', old, executable=executable)
else:
    def set_find_links(executable = sys.executable): ...


    def make_natten_package_command(natten_version, executable = sys.executable, is_link_mode = False):
        return [f'natten=={natten_version}']


    def unset_find_links(old, executable = sys.executable): ...


def install_natten(natten_version, executable = sys.executable):
    pypi.install(make_natten_package_command(natten_version, executable), executable)


def parent_python():
    parent_process = psutil.Process(os.getppid())
    return parent_process.exe()