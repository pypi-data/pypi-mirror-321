from setuptools import setup, find_packages

setup(
    name="Topsis-Akshita-102203527",
    version="0.1.0",
    author="Akshita",
    author_email="akshita.chauhan1414@gmail.com",
    description="A Python package for implementing the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Akshita1414/Topsis-Akshita-102203527.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
    ],
)
