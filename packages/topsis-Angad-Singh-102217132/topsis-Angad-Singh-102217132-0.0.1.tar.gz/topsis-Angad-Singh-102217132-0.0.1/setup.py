from setuptools import find_packages, setup

with open('README.md',"r") as f:
    description = f.read()

setup(
    name='topsis-Angad-Singh-102217132',
    packages=find_packages(),
    version='0.0.1',
    author_email='asingh36_be22@thapar.edu ',
    author='Angad Singh',
    license='MIT',
    install_requires=['pandas', 'numpy'],
    long_description=description,
    long_description_content_type="text/markdown",
)