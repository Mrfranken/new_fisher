from flask import Flask, make_response, jsonify, _app_ctx_stack, request
from flask.ctx import AppContext
from .web import web
from .models.book import db

__author__ = 'Vince'


def register_blueprint(app):
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    # 读取配置文件

    app.config.from_pyfile('config.py')
    app.config.from_pyfile('secure.py')
    # app.config.from_object('app.config')
    register_blueprint(app)
    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():  # 实际上等价于AppContext(app).push()
        db.create_all()
    return app
