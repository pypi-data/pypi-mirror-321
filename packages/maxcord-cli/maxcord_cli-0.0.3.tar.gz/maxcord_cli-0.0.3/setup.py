from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="maxcord-cli",
    version="0.0.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "maxcord-cli=maxcord_cli.main:main",
        ],
    },
    install_requires=[],
    description="CLI for easy discord cogs creation.",
    long_description = long_description,
    author="omaxpy",
    author_email="moukasland@gmail.com",
    url="https://github.com/omaxpy/maxcord-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.9",
)