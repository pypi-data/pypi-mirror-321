import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# This call to setup() does all the work
setup(
    name="Topsis-Kirtan-102203600",
    version="1.0.0",
    description="It Ranks the Models based on MCDM",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/KirtanDwivedi/Topsis-Kirtan-102203600",
    author="Kirtan Dwivedi",
    author_email="kirtand02@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)