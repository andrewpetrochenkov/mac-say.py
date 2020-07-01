import setuptools

setuptools.setup(
    name='mac-say',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
