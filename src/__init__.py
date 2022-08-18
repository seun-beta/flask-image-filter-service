import os

from flask import Flask

from dotenv import load_dotenv
from flasgger import Swagger

from src.config.swagger import swagger_config, template
from src.image.api import image_filter_bp

load_dotenv()


def check_environment_variables():

    SECRET_KEY = os.environ.get("SECRET_KEY")
    if SECRET_KEY is None:
        raise Exception("SECRET_KEY does not exist")

    return SECRET_KEY


def create_app(test_config=None):
    app: Flask = Flask(__name__, instance_relative_config=True)

    env_vars = check_environment_variables()

    if not test_config:
        app.config.from_mapping(SECRET_KEY=env_vars[0])
    else:
        app.config.from_mapping(test_config)

    # Swagger configuration
    Swagger(app=app, config=swagger_config, template=template)

    # Register blueprints
    app.register_blueprint(image_filter_bp)

    return app
