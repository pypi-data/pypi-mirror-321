from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data_governance_checkup",
    version="0.1.2",
    author="Pratik P. Lahudkar",
    author_email="pratik.lahudkar@gmail.com",
    description="A library to simplify and enhance data governance and compliance processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratiklahudkar/data-governance",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
