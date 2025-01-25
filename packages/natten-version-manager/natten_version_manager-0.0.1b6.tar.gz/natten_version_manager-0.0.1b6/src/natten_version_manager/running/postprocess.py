import subprocess
import os
import sys


_site_packages_command = """
import site
print(site.getsitepackages()[0])
"""


def get_site_packages_path(executable = sys.executable):
    return subprocess.run([executable, '-c', _site_packages_command], capture_output=True, text=True).stdout[:-1]


def delete_package_meta(name, version, executable = sys.executable):
    site_packages_path = get_site_packages_path(executable)
    name = name.replace('-', '_')
    dist_info_path = os.path.join(site_packages_path, f'{name}-{version}.dist-info')
    egg_info_path = os.path.join(site_packages_path, f'{name}-{version}.egg-info')
    command = f"""
import process
import shutil
import os
while process.is_process_alive({os.getppid()}): ...
dist_info_path = '{dist_info_path}'
if os.path.exists(dist_info_path):
    shutil.rmtree(dist_info_path)
egg_info_path = '{egg_info_path}'
if os.path.exists(egg_info_path):
    shutil.rmtree(egg_info_path)
"""
    subprocess.Popen([executable, '-c', command])