from setuptools import setup, find_packages

setup(
    name= 'p1 libs',
    version= '0.1.0',
    packages= find_packages(include=['p1', 'p1.*'])
)
