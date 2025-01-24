from configparser import ConfigParser
from io import open
from pathlib import Path

from setuptools import setup

from zappa_packer import __version__

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

pipfile = ConfigParser()
pipfile.read(Path(__file__).parent.resolve() / "Pipfile")
"""required = [
    "{}{}".format(name, version.strip('"')) if version != '"*"' else name for name, version in pipfile["packages"].items()
]
test_required = [
    "{}{}".format(name, version.strip('"')) if version != '"*"' else name for name, version in pipfile["dev-packages"].items()
]"""

# Handle missing sections gracefully
required = []
if 'packages' in pipfile:
    for name, version in pipfile["packages"].items():
        version = version.strip('"')
        # Remove the "*" version constraint to handle "any version" scenario
        print(name, " asdasd " ,version)
        if version == '*':
            required.append(name)
        else:
            required.append(f"{name}{version}")

test_required = []
if 'dev-packages' in pipfile:
    for name, version in pipfile["dev-packages"].items():
        version = version.strip('"')
        # Remove the "*" version constraint to handle "any version" scenario
        if version == '*':
            test_required.append(name)
        else:
            test_required.append(f"{name}{version}")

setup(
    name="zappa-packer",
    version=__version__,
    packages=["zappa_packer"],
    install_requires=required,
    python_requires=">=3.7",
    tests_require=test_required,
    include_package_data=True,
    license="MIT License",
    description="Server-less Python Web Services for AWS Lambda and API Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mariowix/ZappaPacker",
    author="Mario Mixtega",
    author_email="mariomixtega@yahoo.com",
    entry_points={
        "console_scripts": [
            "zappa-packer=zappa_packer.cli:handle",
            "zp=zappa_packer.cli:handle",
        ]
    },
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)