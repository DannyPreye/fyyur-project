import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://kvjksnthxbusgr:ef61fa014b30f99c3741751a6080e46746cd01f219f8246b4d05bd49f4c16872@ec2-54-147-33-38.compute-1.amazonaws.com:5432/d56n6ommgaf7ic'
SQLALCHEMY_TRACK_MODIFICATIONS = False
