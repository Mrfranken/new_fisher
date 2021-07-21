# -*- coding: utf-8 -*-
# 千万千万不要将 127.0.0.1 写成 localhost
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8823443wsj_WIN@127.0.0.1:3306/new_fisher'  # pip install cymysql
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '8823443wsj_WIN'

"""
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
"""
