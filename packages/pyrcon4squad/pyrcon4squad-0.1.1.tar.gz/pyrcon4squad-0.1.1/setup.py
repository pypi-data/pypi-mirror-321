# setup.py
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pyrcon4squad",
    version="0.1.1",
    author="guyuemochen",
    packages=find_packages(),
    description="A simple python rcon package for squad",
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
