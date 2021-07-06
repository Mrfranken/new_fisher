from flask import Flask, make_response, jsonify
from app.web import web

__author__ = 'Vince'


def register_blueprint(app):
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    # 读取配置文件
    app.config.from_pyfile('config.py')
    # app.config.from_object('app.config')
    register_blueprint(app)
    return app
