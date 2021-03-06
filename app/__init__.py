import platform
from flask_login import LoginManager
from flask import Flask, make_response, jsonify, _app_ctx_stack, request
from flask.ctx import AppContext
login_manager = LoginManager()

from .web import web
from .models import db


__author__ = 'Vince'


def register_blueprint(app):
    app.register_blueprint(web)


def init_login_manager(app):
    login_manager.init_app(app)


def create_app():
    app = Flask(__name__)
    # app = Flask(__name__)
    # 读取配置文件
    app.config.from_pyfile('config.py')
    if 'mac' in platform.platform():
        app.config.from_pyfile('mac_secure.py')
    else:
        app.config.from_pyfile('win_secure.py')
    # app.config.from_object('app.config')
    register_blueprint(app)

    db.init_app(app)

    login_manager.init_app(app)

    # db.create_all(app=app)
    with app.app_context():  # 实际上等价于AppContext(app).push()
        db.create_all()
    return app
