from setuptools import setup, find_packages

setup(
    name="Py3dObj", 
    version="1.0",
    author="Vlad",
    description="Module for creating 3D models using Python in .obj format",
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=1.0'
)