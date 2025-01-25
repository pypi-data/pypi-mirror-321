import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Garima-102203385",
    version="1.0.0",
    description="Perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) analysis on a dataset.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/garimaahuja112/Topsis-Garima-102203385",
    author="Garima Ahuja",
    author_email="garimaahuja217@gmail.com",  # Update with your email
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["topsis"],  # The package name corresponds to the 'topsis' folder
    include_package_data=True,
    install_requires=["pandas", "numpy"],  # Dependencies
    entry_points={
        "console_scripts": [
            "topsis=topsis.102203385:main",  # Assuming your main function is inside 102203385.py
        ]
    },
)
