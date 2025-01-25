from setuptools import setup
# Read the content of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(name="topsis_102203992",version=1.1,
description="Package for Topsis Score Calculation",author="Ishita Garg",long_description=long_description,
long_description_content_type="text/markdown",
packages=['topsis_102203992'],
install_requires=[
        "pandas>=1.0.0",  # Specifies pandas as a prerequisite with a minimum version of 1.0.0
        "numpy>=1.18.0"]
)