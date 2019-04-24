from flask import Flask
from flask_migrate import Migrate
from db_model import Post


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')

    from database import db
    db.init_app(app)
    Migrate(app, db, directory='migrations')

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


