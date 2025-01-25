from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Gautam-102217084",
    version="1.0.0",
    author="Gautam Garg",
    author_email="ggarg1_be22@thapar.edu",
    url="https://github.com/GautamGarg04/Topsis-Gautam-102217084",
    description="A python package for implementing topsis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis-gautam=Topsis_Gautam_102217084.topsis:main"
        ]
    },
)