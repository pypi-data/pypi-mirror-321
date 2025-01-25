from setuptools import setup, find_packages

# Read README.md with UTF-8 encoding
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="topsis_Tanisha_102203818",  # Your original name
    version="0.1.2",  # Your original version
    description="A Python package for implementing TOPSIS for multi-criteria decision making",
    author="Tanisha",  # Your original author
    author_email="tanishajain286@gmail.com",  # Your original email
    url="https://github.com/tanisha1234-sys/topsis-tanisha-102203818",  # Your original URL
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
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
            "topsis=topsis.topsis:main",
        ],
    },
)