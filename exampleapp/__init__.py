import os
from config import configure_app

from flask_api import FlaskAPI
from exampleapp.api import api

def create_app(test_config=None):
    # create and configure the app
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # Load the default configuration
        configure_app(app)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(api, url_prefix='/api')

    return app