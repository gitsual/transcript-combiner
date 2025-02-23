from setuptools import setup, find_packages

setup(
    name="transcript-combiner",
    version="1.0.0",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "spacy>=3.0.0",
        "gitpython>=3.1.0",
    ],
    python_requires=">=3.8",
    author="gitsual",
    author_email="alvarogs_98@hotmail.com",
    description="A tool to combine transcripts to create a unified version",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
) 