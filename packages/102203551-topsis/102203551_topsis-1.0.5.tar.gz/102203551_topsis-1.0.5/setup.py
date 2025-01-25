import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102203551-topsis",  # Package name should be unique and descriptive
    version="1.0.5",           # Initial version of your package
    description="A Python package to implement the TOPSIS decision-making method.",  # Short description
    long_description=README,   # Long description from README.md
    long_description_content_type="text/markdown",  # Content type for README
    url="https://github.com/Aryanz01/topsis-python-package",  # Replace with your actual GitHub repo URL
    author="Aryan Vashishth",  # Your name
    author_email="avashishth_be22@thapar.edu",  # Your email
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
    packages=["topsis"],  # The name of the folder containing your package code
    include_package_data=True,  # Include other files specified in MANIFEST.in
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],  # Dependencies required for your project
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",  # Command-line tool mapping
        ]
    },
)
