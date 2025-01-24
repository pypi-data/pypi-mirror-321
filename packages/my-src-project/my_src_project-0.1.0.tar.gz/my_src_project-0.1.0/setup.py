#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2025 - 2025 Guanhao Sun, Inc. All Rights Reserved 
#
# @Time    : 2025/1/15 10:03
# @Author  : Guanhao Sun
# @File    : setup.py
# @IDE     : PyCharm

# setup.py
from setuptools import setup, find_packages

setup(
    name="my_src_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": ["pytest"],
    },
)
