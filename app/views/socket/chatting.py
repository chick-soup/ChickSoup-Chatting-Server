from flask_socketio import Namespace, emit


class chattingNamespace(Namespace):
    def on_connect(self):
        emit('add', {'status':'300'})