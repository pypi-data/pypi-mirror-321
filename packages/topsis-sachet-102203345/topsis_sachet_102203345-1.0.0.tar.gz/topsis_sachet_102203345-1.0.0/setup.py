# setup.py
from setuptools import setup, find_packages

setup(
    name="topsis_sachet_102203345",  
    version="1.0.0",  
    author="Sachet Singh",
    author_email="srawat_be22@thapar.edu",
    description="A Python package to perform TOPSIS analysis on datasets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sachetsinghrawat/topsis_sachet_102203345", 
    packages=find_packages(),
    py_modules=["main"],  
    entry_points={
        "console_scripts": [
            "topsis=topsis:main",  
        ],
    },
    install_requires=[
        "pandas>=1.0.0", 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
