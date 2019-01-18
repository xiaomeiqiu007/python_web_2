# coding: utf-8
# auth:小煤球
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import os
DEBUG = True
SECRET_KEY = "dropseckey123"

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'desc'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False