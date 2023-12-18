from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='JoeriAbboClients',
    version='master',
    packages=find_packages(),
    install_requires=required
)
