from setuptools import setup, find_packages

setup(
    name="topsis-shubhaan-102203456",
    version="0.2.0",
    author="Shubhaan Bhandari",
    author_email="shubhaan2004@gmail.com",
    description="A Python package for the TOPSIS method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shubhaan06/topsis",
    packages=find_packages(),
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