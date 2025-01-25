from setuptools import setup, find_packages

setup(
    name="excel_unpack",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "olefile",
    ],
    entry_points={
    "console_scripts": [
        "excel-unpack=excelunpack.cli:main"
    ],
    },

    author="Shivnand Vishwakarma",
    description="A tool to extract attachments from Excel (XLSX) files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/svk1998/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
