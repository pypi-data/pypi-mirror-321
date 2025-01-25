from setuptools import setup, find_packages
from setuptools.command.bdist_wheel import bdist_wheel, safer_name, safer_version
import os
import subprocess
from wheel.wheelfile import WheelFile
from zipfile import ZipFile
from .. import natten_installer as ni


_site_packages_command = """
import site
print(site.getsitepackages()[0])
"""
def _get_site_packages_path(executable):
    return subprocess.run([executable, '-c', _site_packages_command], capture_output=True, text=True).stdout[:-1]


class Setup:
    def make_install_requires(self, version):
        self.executable = ni.parent_python()
        command, self.combined_version = ni.make_natten_package_command(version, self.executable, True, True)
        return command
    
    @classmethod
    def make_dist_info(cls, name, version):
        name = safer_name(name)
        version = safer_version(version)
        distinfo_dirname = f'{name}-{version}.dist-info'
        return distinfo_dirname
    
    def post_build_dist_wheel(self, bdw: bdist_wheel):
        impl_tag, abi_tag, plat_tag = bdw.get_tag()
        archive_basename = f"{bdw.wheel_dist_name}-{impl_tag}-{abi_tag}-{plat_tag}"
        wheel_path = os.path.join(bdw.dist_dir, archive_basename + ".whl")
        temp_wheel_path = f'{wheel_path[:-4]}-temp.whl'
        os.rename(wheel_path, temp_wheel_path)
        subprocess.run([self.executable, '-c', f"print('事实上，{os.listdir(bdw.dist_dir)}')"])
        
        distinfo_dirname = self.make_dist_info(bdw.distribution.get_name(), bdw.distribution.get_version())
        natten_distinfo_dirname = self.make_dist_info('natten', self.combined_version)
        natten_distinfo_path = os.path.join(_get_site_packages_path(self.executable), natten_distinfo_dirname)
        natten_record_path = os.path.join(natten_distinfo_path, 'RECORD')
        with open(natten_record_path, 'r') as f:
            natten_record = f.read()

        with ZipFile(wheel_path, 'w', compression=bdw._zip_compression()) as wf:
            with WheelFile(temp_wheel_path, 'r', bdw._zip_compression()) as wf_temp:
                for file_name in wf_temp.namelist():
                    with wf_temp.open(file_name) as f:
                        if file_name == f'{distinfo_dirname}/RECORD':
                            this_record = f.read().decode()
                            new_record = f'{natten_record}{this_record}'
                            wf.writestr(file_name, new_record)
                        else:
                            wf.writestr(file_name, f.read().decode())
        
        os.remove(temp_wheel_path)
        
        with open(natten_record_path, 'w+') as f:
            f.write(this_record)

    @classmethod
    def run(cls, name, version):
        instance = cls()
        
        
        class PostBuildDistWheel(bdist_wheel):
            def run(self):
                super().run()
                instance.post_build_dist_wheel(self)


        setup(
            name=name,
            version=version,
            install_requires=instance.make_install_requires(version),
            packages=find_packages(),
            cmdclass={
                'bdist_wheel': PostBuildDistWheel,
            },
        )