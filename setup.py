#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.md").read()
doclink = """
Documentation
-------------

The full documentation is at http://django-ai-channels.rtfd.org."""
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="django-ai-channels",
    version="0.1.0",
    description="Browser generated AI events over channels",
    long_description=readme + "\n\n" + doclink + "\n\n" + history,
    author="Dino Livanos",
    author_email="dino.livanos@gmail.com",
    url="https://github.com/dinolivanos/django-ai-channels",
    packages=[
        "aichannels",
    ],
    package_dir={"aichannels": "aichannels"},
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords="django-ai-channels",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
