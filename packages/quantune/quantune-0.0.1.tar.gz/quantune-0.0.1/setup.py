from setuptools import setup, find_packages

VERSION = "0.0.1"

with open("README.md", encoding="utf-8") as readme_fh:
    readme = readme_fh.read()

with open("requirements.txt", "r") as requirements_fh:
    requirements = requirements_fh.read().split()

setup(
    name="quantune",
    version="0.0.1",
    author="Neocosmicx",
    author_email="sejanbagani14@gmail.com",
    description="Quantune is the tune for Quantum computing.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Neocosmicx-Quantum/Quantune",
    packages=find_packages(exclude=["test"]),
    classifiers=[
        "Programming Language :: Python",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
)
