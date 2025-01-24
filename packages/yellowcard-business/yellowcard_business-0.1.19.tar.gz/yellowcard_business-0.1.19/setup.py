from setuptools import setup, find_packages
import pathlib

# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

def read_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='yellowcard_business',
    version='0.1.19',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),  # Use requirements.txt
    description='Python SDK for the YellowCard B2B API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yellowcard B2B API Team',
    author_email='your.email@example.com',
    url='https://docs.yellowcard.engineering/',
)
