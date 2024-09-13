from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import Config

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from Portal.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app