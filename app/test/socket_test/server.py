from flask_socketio import SocketIO
from flask import Flask


app = Flask(__name__)

socketio = SocketIO(app)



if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5555)