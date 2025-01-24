from setuptools import setup, find_packages

setup(
    name="Topsis-Rohit-102203804",
    version="1.0.0",
    author="Rohit Singla",
    author_email="rsingla_be22@thapar.edu",
    description="Implementation of TOPSIS for multi-criteria decision making",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/therohitsingla/topsis-pypi",
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
