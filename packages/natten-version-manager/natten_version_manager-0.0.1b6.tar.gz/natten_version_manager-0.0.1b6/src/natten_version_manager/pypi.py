import sys
import subprocess
import requests


def make_install_command(name, executable = sys.executable):
    return [executable, '-m', 'pip', 'install', name]


def install(name, executable = sys.executable, hide_output = False):
    subprocess.run(make_install_command(name, executable), check=True, capture_output=hide_output)


def make_uninstall_command(name, executable = sys.executable):
    return [executable, '-m', 'pip', 'uninstall', '-y', name]


def uninstall(name, executable = sys.executable, hide_output = False):
    subprocess.run(make_uninstall_command(name, executable), check=True, capture_output=hide_output)


def config_get(key, scope = 'global', executable = sys.executable):
    try:
        process = subprocess.run([executable, '-m', 'pip', 'config', 'get', f'{scope}.{key}'], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        return None
    return process.stdout[:-1]


def config_set(key, value, scope = 'global', executable = sys.executable):
    subprocess.run([executable, '-m', 'pip', 'config', 'set', f'{scope}.{key}', value], capture_output=True)


def config_unset(key, scope = 'global', executable = sys.executable):
    subprocess.run([executable, '-m', 'pip', 'config', 'unset', f'{scope}.{key}'], capture_output=True)


def get_latest_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latest_version = data['info']['version']
        return latest_version
    return None