from flask import Flask
from flaskr import blueprints
from flaskr.extensions import db
from flaskr.models import create_database_tables

DEVELOPMENT_ENV = True


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    register_extensions(app)
    register_blueprints(app)
    create_database_tables(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    return None


def register_blueprints(app: Flask):
    app.register_blueprint(blueprints.views.blueprint)
    return None
