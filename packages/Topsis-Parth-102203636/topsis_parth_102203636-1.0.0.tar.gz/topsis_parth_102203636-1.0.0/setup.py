import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Parth-102203636",
    version="1.0.0",
    description="Multiple criteria decision making for selection of best model",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ParthA164/Topsis-Parth-102203636",
    author="Parth Adlakha",
    author_email="parthmris92@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["topsis_package"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis_package=topsis_package.__main__:main",
        ]
    },
)