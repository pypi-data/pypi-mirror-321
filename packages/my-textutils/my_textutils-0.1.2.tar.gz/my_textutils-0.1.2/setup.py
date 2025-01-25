from setuptools import setup, find_packages
from pathlib import Path
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="my_textutils",
    version="0.1.2",
    description="A utility library for text processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kaushal Varma",
    author_email="varma.kaushal.99@gmail.com",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
