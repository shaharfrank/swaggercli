import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaggercli",
    version="0.0.1",
    author="Shahar Frank",
    author_email="shahar.frank@example.com",
    description="An auto-generating CLI for swagger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaharfrank/swaggercli",
    scripts=['swaggercli.py']
    install_requires=[
          'multilevelcli',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
