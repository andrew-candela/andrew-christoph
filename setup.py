import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # we don't intend to upload this to PyPi, so don't worry too much about
    # name, version etc
    name="CansAndString",
    version="0.0.1",
    description="Communicate through AWS Kinesis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)
