from flask import Flask
from flask_socketio import SocketIO


def create_app(*config_cls):
    flask = Flask(__name__)

    for config in config_cls:
        flask.config.from_object(config)

    socketIO = SocketIO(flask)

    return flask, socketIO