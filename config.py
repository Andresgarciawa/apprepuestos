import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_desarrollo'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///tienda.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cerulean'