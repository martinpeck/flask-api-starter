import os

config = {
    "development": "config.development",
    "production": "config.production",
    "default": "config.default"
}

def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config['default'])
    app.config.from_object(config[config_name])