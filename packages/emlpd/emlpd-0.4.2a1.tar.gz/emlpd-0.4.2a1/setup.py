#!/usr/bin/env python

import re
import setuptools

from emlpd.gameapi import VER_STRING

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emlpd",
    version=VER_STRING,
    author="REGE",
    author_email="junyu336699@sina.com",
    description="Python 小游戏 API 及实现：恶魔轮盘赌",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/cheny0y0/emlpd",
    packages=setuptools.find_packages(exclude=("test")),
    classifiers=(
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Turn Based Strategy"
    )
)
