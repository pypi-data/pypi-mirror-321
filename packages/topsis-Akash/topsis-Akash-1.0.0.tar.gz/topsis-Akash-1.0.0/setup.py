from setuptools import setup, find_packages

setup(
    name="topsis-Akash", 
    version="1.0.0",  
    author="Akash Kohli",  
    author_email="akashkohli1202@gmail.com", 
    description="A Python package to implement the TOPSIS method for decision making.",
    long_description=open("README.md").read(), 
    long_description_content_type="text/markdown",
    url="https://github.com/Akashkohli28/topsis-akash",  
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.19.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)