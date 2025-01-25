from setuptools import setup,find_packages
import socket,subprocess

setup(
    name="mymo",           # Your package name
    version="1.0",            # Version of your package
    description="sample module",  # Short description
    author="mohamed1234",         # Your name
    author_email="mohamedhathim628@gmail.com",   # Your email
    packages=find_packages(),   # Automatically find the `my_module` package
    python_requires=">=3.6",    #
)

