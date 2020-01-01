from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

@app.route('/')
def index():
    return 'INDEX'

@sio.on('connect')
def connect():
    print('[-] CONENCT')

@sio.on('disconnect')
def disconnect():
    print('[-] DISCONNECT')

@sio.on('chat')
def chatting(*data):
    print('[-] WHOS')
    emit('getChat', data)
    print(data)


sio.run(app, host='0.0.0.0', port=3333)