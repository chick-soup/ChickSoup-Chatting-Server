import os


class localLevelConfig:
    ENV = 'Local'
    DEBUG = True
    SECRET_KEY = 'secretKey'


class productionLevelConfig:
    ENV = 'Production'
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')