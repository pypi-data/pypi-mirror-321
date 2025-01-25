import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102203201-simrat",
    version="1.0.0",
    description="It gives the topsis analysis of your csv file with score and rankings.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/simratk05/topsis_py_package_simrat",
    author="Simrat Kaur",
    author_email="simrat.kms@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["simrat"],
    include_package_data=True,
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "simtopsis=simrat.__main__:main",
        ]
    },
)