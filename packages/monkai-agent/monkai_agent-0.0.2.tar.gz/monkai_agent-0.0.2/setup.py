from setuptools import find_packages, setup

def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()
        
setup(
    name='monkai_agent',
    packages=find_packages(include=['monkai_agent', 'monkai_agent.*']),
    version='0.0.2',
    description='Monkai Agent Library',
    author='Monkai Team',
    install_requires=parse_requirements('requeriment.txt'),
)