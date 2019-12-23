import os


class localLevelConfig:
    ENV = 'Local'
    DEBUG = True
    SECRET_KEY = 'secretKey'
    ELASTIC_APM = {
        'SERVICE_NAME': 'chick_test_apm',
        'SECRET_TOKEN': 'secretToken',
        'DEBUG': True
    }

class productionLevelConfig:
    ENV = 'Production'
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    ELASTIC_APM = {
        'SERVICE_NAME': os.getenv('CHICK_SERVICE'),
        'SECRET_TOKEN': os.getenv('SECRET_TOKEN')
    }