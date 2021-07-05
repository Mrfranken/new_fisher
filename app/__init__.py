from flask import Flask, make_response, jsonify
from app.web import web

__author__ = 'Vince'


def register_blueprint(app):
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    register_blueprint(app)
    return app
