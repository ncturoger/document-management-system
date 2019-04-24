from flask import Flask, jsonify
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

    @app.route('/check')
    def check():
        response = {'response': 'ok'}
        content = []
        datas = Post.query.all()
        if datas:
            for data in datas:
                content.append({'title': data.title, 'content': data.content})

        response['result'] = content
        return jsonify(response)

    return app


