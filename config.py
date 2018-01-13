#from app import app
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'instance', 'data.db')
DEBUG = False
