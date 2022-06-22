import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://jcmwuirpcjmcgs:0e0577e17196f9a2186c3dfdaeb7e1150e7b718ed227a5089ddae976875adbb3@ec2-52-72-56-59.compute-1.amazonaws.com:5432/dckqc79qhsaamu'
SQLALCHEMY_TRACK_MODIFICATIONS = False
