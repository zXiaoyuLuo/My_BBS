#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Time    : 2024/4/2 17:41
# @Author  : Sepine Tam
# @File    : config.py.py
# @IDE     : PyCharm
# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a default secret key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'mybbs.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
