from setuptools import setup, find_packages
from setuptools.command.install import install
from .. import natten_installer as ni
from .postprocess import delete_package_meta


class Setup:
    def __init__(self):
        self.executable = None

    def make_install_requires(self, version):
        self.executable = ni.parent_python()
        return ni.make_natten_package_command(version, self.executable, True)
        
    def post_installation(self, installation: install):
        delete_package_meta(installation.distribution.name, installation.distribution.version, self.executable)

    @classmethod
    def run(cls, name, version):
        instance = cls()
        
        
        class PostInstallation(install):
            def run(self):
                super().run()
                instance.post_installation(self)


        setup(
            name=name,
            version=version,
            install_requires=instance.make_install_requires(version),
            packages=find_packages(),
            cmdclass={
                'install': PostInstallation,
            },
        )