from setuptools import setup, find_packages

setup(
    name="Topsis-Trish_Rustagi-102203584",
    version="0.1.0",
    author="Trish Rustagi",
    author_email="trishrustagi@gmail.com",
    description="A Python package for implementing the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trish-r/Topsis-Trish_Rustagi-102203584.git",
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
