from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    ''' sets flask configuration variables '''
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    DB_URI = environ.get('DB_URI')