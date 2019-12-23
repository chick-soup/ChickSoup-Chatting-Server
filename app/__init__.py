from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

from flask_cors import CORS
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager

from mongoengine import connect
from const import _localDatabaseSetting


def registerExtentions(app: Flask):
    CORS(app, resources={
        r"*": {"origin": "*"},
    })
    JWTManager().init_app(app)
    connect(**_localDatabaseSetting)
    ElasticAPM().init_app(app, **app.config['ELASTIC_APM'])

def registerViews(app: Flask):
    from app.views.apis import room
    app.register_blueprint(room.api.blueprint)


def registerSocketIONamespace(socketApp: SocketIO):
    from app.views.socket.chatting import chattingNamespace
    socketApp.on_namespace(chattingNamespace('/'))


def create_app(*config_cls):
    flask = Flask(__name__)
    socketIO = SocketIO(flask, cors_allowed_origins="*", async_mode="threading")

    for config in config_cls:
        flask.config.from_object(config)

    registerViews(flask)
    registerSocketIONamespace(socketIO)
    registerExtentions(flask)

    return flask, socketIO