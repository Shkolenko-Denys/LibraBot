import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(basedir, 'db/app.db')

MAX_CONTENT_LENGTH = 1024 * 1024

UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'upload/')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

SECRET_KEY = 'you-will-never-guess'

FLASKY_ADMIN = 'root@gmail.com'

SQLALCHEMY_TRACK_MODIFICATIONS = False

TOKEN = "2140017593:AAEggjpYiVfRefiVtpWt2z3kGMqP4TfLy3A"
KEY = "AIzaSyDVCYmlQtwuTj5XgLo_Em9cqZHam3uct20"
