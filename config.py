import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask app configuration
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-WTF CSRF configuration
    WTF_CSRF_ENABLED = True
