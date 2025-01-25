from setuptools import setup, find_packages

setup(
    name="Topsis-Piyush-102217003",
    version="0.1.0",  # Start with version 0.1.0
    author="Piyush Garg",
    author_email="piyushgarg878@gmail.com",
    description="A Python package for implementing Topsis method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/piyushgarg878/Topsis-Piyush-102217003.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy", "pandas"  # Add dependencies here
    ],
)
