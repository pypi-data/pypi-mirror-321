from setuptools import setup, find_packages

setup(
    name="topsis-Pranav-102216023",
    version="0.1.0",
    author="Pranav Duggal",
    description="A Python package for performing TOPSIS analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pranav07Duggal/UCS654/blob/main/102216023.py",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)