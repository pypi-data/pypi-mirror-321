import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102203551-square",  # Replace with your package name
    version="1.0.0",           # Your package version
    description="It squares the number",  # Short description of the package
    long_description=README,   # Long description from README file
    long_description_content_type="text/markdown",  # Content type for README
    url="https://github.com/Aryanz01",  # Replace with your repo URL
    author="Aryan Vashishth",  # Your name
    author_email="avashishth_be22@thapar.edu",  # Replace with your email
    license="MIT",             # License type
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=["square"],  # Replace with your package folder name
    include_package_data=True,
    install_requires=[],     # List dependencies here, e.g., ["numpy"]
    entry_points={
        "console_scripts": [
            "square=square.__main__:main",
        ]
    },    
)
