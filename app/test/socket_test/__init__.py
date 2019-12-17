import socketio


sio = socketio.Client()

@sio.event()
def connect():
    print('[CONNECT]')


@sio.event()
def disconnect():
    print('[DISCONNECT]')

sio.connect('http://127.0.0.1:3000/')