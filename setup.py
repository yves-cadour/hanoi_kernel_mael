
from setuptools import setup, find_packages

setup(
    name='HanoiKernel',
    version='0.1',
    url='https://github.com/babert-Mael/hanoi_kernel',
    author='Babert Maël',
    author_email='babert-m@saint-louis29.net',
    description='The core of the hanoi game',
    packages=find_packages(),   
    install_requires=['Stack'],
)
