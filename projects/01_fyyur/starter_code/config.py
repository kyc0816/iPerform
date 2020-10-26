import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# 1025 created db and put it into config, which will be called as 
# app.config.from_object('config')
# at app.py
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:1111@localhost:5432/db_fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
