import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-supercluster",
    version="0.0.1",
    author="Hugo Laplace-Builhe",
    author_email="builhe@hotmail.fr",
    description="A python implementation of the JS lib SuperCluster by mapbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sangrene/python-supercluster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)