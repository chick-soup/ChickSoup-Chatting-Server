from flask import Flask
from flask_socketio import SocketIO


def registerViews(app: Flask):
    from app.views.apis import createRoom
    app.register_blueprint(createRoom.api.blueprint)


def registerSocketIONamespace(socketApp: SocketIO):
    from app.views.socket.chatting import testNamespace
    socketApp.on_namespace(testNamespace('/'))

def create_app(*config_cls):
    flask = Flask(__name__)
    socketIO = SocketIO(flask)

    for config in config_cls:
        flask.config.from_object(config)

    registerViews(flask)
    registerSocketIONamespace(socketIO)

    return flask, socketIO