import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis-archie-102203826",
    version="1.0.0",
    description="Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abajaj15/102203826_topsis",
    author="Archie Bajaj",
    author_email="archiebajaj4@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis102203826=topsis.__main__:main",
        ]
    },
)