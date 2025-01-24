#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2025 - 2025 Guanhao Sun, Inc. All Rights Reserved 
#
# @Time    : 2025/1/15 9:52
# @Author  : Guanhao Sun
# @File    : module1.py
# @IDE     : PyCharm

from imgrender import render


def shell_img(path, shape=(60, 60)):
    render(path, shape)


if __name__ == "__main__":
    render('tkfgs.png')
