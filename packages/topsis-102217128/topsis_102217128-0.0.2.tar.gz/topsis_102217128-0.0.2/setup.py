from setuptools import find_packages, setup

with open('README.md',"r") as f:
    description = f.read()

setup(
    name='topsis-102217128',
    packages=find_packages(),
    version='0.0.2',
    author_email='ksingh11_be22@thapar.edu',
    author='Karanjot Singh',
    license='MIT',
    install_requires=['pandas', 'numpy'],
    long_description=description,
    long_description_content_type="text/markdown",
)