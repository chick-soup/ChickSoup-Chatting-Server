from flask import Flask
from flask_socketio import SocketIO


def register_views(app: Flask):
    from app.views.apis import createRoom
    app.register_blueprint(createRoom.api.blueprint)


def create_app(*config_cls):
    flask = Flask(__name__)

    for config in config_cls:
        flask.config.from_object(config)

    register_views(flask)

    socketIO = SocketIO(flask)

    return flask, socketIO