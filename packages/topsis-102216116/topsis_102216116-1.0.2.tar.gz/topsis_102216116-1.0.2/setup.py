from setuptools import setup, find_packages

setup(
    name="topsis-102216116",
    version="1.0.2",
    author="Naman Babbar",
    author_email="nbabbar_be22@thapar.edu",
    description="A CLI tool for TOPSIS decision-making",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nmnbabbar/topsis-cli",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
