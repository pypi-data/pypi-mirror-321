import pathlib
import setuptools

from gfz_client.__version__ import version


package_data = {"gfz_client": ["CHANGELOG.md", "LICENSE"]}


setuptools.setup(
    name="gfz_api_client",
    version=version,
    author="Maksim Tulin",
    description="GFZ Helmholtz Centre for Geosciences Web Service API Client",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/mmatroskin/gfz_api_client",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_dir={"gfz_client": "./gfz_client"},
    package_data=package_data,
    license_files=["LICENSE"],
    # license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
    install_requires=pathlib.Path("requirements/lib.txt").read_text().split(),
)
