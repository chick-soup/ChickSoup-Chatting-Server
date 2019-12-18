from flask import Flask

from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager


def registerHooks(app: Flask):
    JWTManager().init_app(app)


def registerViews(app: Flask):
    from app.views.apis import room
    app.register_blueprint(room.api.blueprint)


def registerSocketIONamespace(socketApp: SocketIO):
    from app.views.socket.chatting import chattingNamespace
    socketApp.on_namespace(chattingNamespace('/'))


def create_app(*config_cls):
    flask = Flask(__name__)
    socketIO = SocketIO(flask)

    for config in config_cls:
        flask.config.from_object(config)

    registerViews(flask)
    registerSocketIONamespace(socketIO)
    registerHooks(flask)

    return flask, socketIO