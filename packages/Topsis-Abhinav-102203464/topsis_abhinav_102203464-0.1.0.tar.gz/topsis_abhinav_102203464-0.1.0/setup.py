from setuptools import setup, find_packages

setup(
    name="Topsis-Abhinav-102203464",
    version="0.1.0",
    author="Abhinav",
    author_email="ashukla_be22@thapar.edu",
    description="A Python package for implementing the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Topsis-Akshita-102203527",
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