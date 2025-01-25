from setuptools import setup, find_packages
from os import path

# Načítanie obsahu README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="lowkernels",
    version="0.1.1",  # verzia
    packages=find_packages(),
    description="A small tool to create low-kernel operating system using C. Learn more at lowkernels.readthedocs.io",
    long_description=long_description,  # Pridaný long description
    long_description_content_type='text/markdown',  # Typ formátu, ak je README v Markdown
    author="lowkernels",
    license="MIT",
)
