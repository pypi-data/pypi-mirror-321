from setuptools import setup, find_packages
from setuptools.command.install import install
from .. import natten_installer as ni


class Setup:
    def __init__(self):
        self.find_links = None
        self.executable = None

    def make_install_requires(self, version):
        self.executable = ni.parent_python()
        self.find_links = ni.set_find_links(self.executable)
        return ni.make_natten_package_command(version, self.executable)
        
    def post_installation(self, installation: install):
        ni.unset_find_links(self.find_links, self.executable)

    @classmethod
    def run(cls, version):
        instance = cls()
        
        
        class PostInstallation(install):
            def run(self):
                super().run()
                instance.post_installation(self)


        setup(
            name='fit-natten',
            version=version,
            install_requires=instance.make_install_requires(version),
            packages=find_packages(),
            cmdclass={
                'install': PostInstallation,
            },
        )