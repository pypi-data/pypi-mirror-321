import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE /"README.md").read_text()

setup(
    name="102217236-TOPSIS",
    version="1.0.0",
    description="Topsis Implementation.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Anmol Singh",
    author_email="anmolcodess@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["102217236_topsis"],
    include_package_data=True,
    install_requires=["numpy", "pandas", "openpyxl"]
)

