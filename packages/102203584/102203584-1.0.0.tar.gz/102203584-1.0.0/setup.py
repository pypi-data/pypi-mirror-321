import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102203584",
    version="1.0.0",
    description="It performs topsis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/trish-r/102203584-topsis",
    author="Trish Rustagi",
    author_email="trishrustagi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["Fin"],
    include_package_data=True,
    install_requires=["pandas","numpy"],
    entry_points={
        "console_scripts": [
            "topsis=Fin.__main__:main",
        ]
    },
)