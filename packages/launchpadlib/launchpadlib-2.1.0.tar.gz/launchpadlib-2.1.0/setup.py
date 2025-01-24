#!/usr/bin/env python3

# Copyright 2008-2024 Canonical Ltd.
#
# This file is part of launchpadlib.
#
# launchpadlib is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, version 3 of the License.
#
# launchpadlib is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with launchpadlib. If not, see <http://www.gnu.org/licenses/>.

"""Setup for the launchpadlib library."""

from setuptools import setup, find_packages


# generic helpers primarily for the long_description
def generate(*docname_or_string):
    marker = ".. pypi description ends here"
    res = []
    for value in docname_or_string:
        if value.endswith(".rst"):
            with open(value) as f:
                value = f.read()
            idx = value.find(marker)
            if idx >= 0:
                value = value[:idx]
        res.append(value)
        if not value.endswith("\n"):
            res.append("")
    return "\n".join(res)


# end generic helpers


install_requires = [
    "httplib2",
    "lazr.restfulclient>=0.14.2",
    "lazr.uri",
]

setup(
    name="launchpadlib",
    version="2.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    author="The Launchpad developers",
    author_email="launchpadlib@lists.launchpad.net",
    maintainer="LAZR Developers",
    maintainer_email="lazr-developers@lists.launchpad.net",
    download_url="https://launchpad.net/launchpadlib/+download",
    description=open("README.rst").readline().strip(),
    long_description=generate("src/launchpadlib/docs/index.rst", "NEWS.rst"),
    license="LGPL v3",
    python_requires=">=3.8",
    install_requires=install_requires,
    url="https://help.launchpad.net/API/launchpadlib",
    project_urls={
        "Source": "https://code.launchpad.net/launchpadlib",
        "Issue Tracker": "https://bugs.launchpad.net/launchpadlib",
        "Documentation": "https://launchpadlib.readthedocs.io/en/latest/",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",  # noqa: E501
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    extras_require={
        "keyring": ["keyring"],
        "docs": ["Sphinx"],
        # Dependencies useful when testing other packages with launchpadlib.
        "testing": [
            "testresources",
            "wadllib",
        ],
        # Dependencies only needed by launchpadlib's own tests.
        "test": [
            "coverage",
            "pytest",
        ],
    },
)
