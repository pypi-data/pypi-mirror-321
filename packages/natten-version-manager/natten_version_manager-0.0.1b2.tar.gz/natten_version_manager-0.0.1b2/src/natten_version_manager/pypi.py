import sys
import subprocess


def make_install_command(name, executable = sys.executable):
    return [executable, '-m', 'pip', 'install', name]


def install(name, executable = sys.executable, hide_output = False):
    subprocess.run(make_install_command(name, executable), check=True, capture_output=hide_output)


def make_uninstall_command(name, executable = sys.executable):
    return [executable, '-m', 'pip', 'uninstall', '-y', name]


def uninstall(name, executable = sys.executable, hide_output = False):
    subprocess.run(make_uninstall_command(name, executable), check=True, capture_output=hide_output)