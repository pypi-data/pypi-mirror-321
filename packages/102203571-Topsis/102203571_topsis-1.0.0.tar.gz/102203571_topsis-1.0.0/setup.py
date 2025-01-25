from setuptools import setup, find_packages

setup(
    name="102203571-Topsis",  
    version="1.0.0", 
    author="Kushagra",  
    author_email="data_kushagra@gmail.com",  
    description="A Python implementation of the TOPSIS method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(), 
    install_requires=[
        "numpy",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
)
