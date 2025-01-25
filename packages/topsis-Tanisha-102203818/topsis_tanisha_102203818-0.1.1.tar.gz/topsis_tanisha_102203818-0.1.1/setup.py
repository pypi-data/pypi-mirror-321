from setuptools import setup, find_packages
from pathlib import Path
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "topsis_Tanisha_102203818",
    version = "0.1.1",
    description = "A Python package for implementing TOPSIS for multi-criteria decision making",
    author = "Tanisha",
    author_email = "tanishajain286@gmail.com",
    url = "https://github.com/tanisha1234-sys/topsis-tanisha-102203818",


    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically find the package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.5",
        "pandas>=1.1.5",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",  # Command-line entry point
        ],
    },
)
