#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2025 - 2025 Guanhao Sun, Inc. All Rights Reserved 
#
# @Time    : 2025/1/15 9:53
# @Author  : Guanhao Sun
# @File    : test_module1.py
# @IDE     : PyCharm

import pytest
from src.my_project.module1 import hello_world


def test_hello_world():
    assert hello_world() == "Hello, world!"
