"""Setup script for image display"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="sampleclass",
    version="1.0.0",
    description="sampleclass package is used to claculate different "
                "mathematical operations like add, multiply, subtract, "
                "division of 2 numbers.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ShashankVBhat/Sample_Class",
    author="shashank",
    author_email="bhatshashank8@gmail.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["my_app"],
    include_package_data=True,
    install_requires=[],
)
