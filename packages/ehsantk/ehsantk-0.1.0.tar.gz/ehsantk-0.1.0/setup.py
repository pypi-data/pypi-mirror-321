from setuptools import setup, find_packages

setup(
    name="ehsantk",
    version="0.1.0",
    author="Ehsaneddin Asgari",
    author_email="asgari@berkeley.edu",
    description="Ehsaneddin's Toolkit: A personal toolkit for research and development",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ehsanasgari/ehsaneddintk",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
