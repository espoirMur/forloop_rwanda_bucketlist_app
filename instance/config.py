import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flask_api.db'
    # for windows sqlite:///c:/tmp/flask_api.db


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
