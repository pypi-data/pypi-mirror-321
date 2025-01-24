from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='yellowcard_business',
    version='0.1.4',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),  # Use requirements.txt
    description='Python SDK for the YellowCard B2B API',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/b2b-api-sdk',
)
