#from app import app
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'instance', 'data.db')
DEBUG = False

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_ROOT,'instance','data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
