import socketio


sio = socketio.Client()

@sio.on('chatData')
def getter(data):
    print(data)

@sio.event()
def connect():
    print('[CONNECT]')


@sio.event()
def disconnect():
    print('[DISCONNECT]')

sio.connect('http://127.0.0.1:3000/')

while True:
    data = input()
    sio.emit('getChat', {
        'roomId': '34567',
        'userId': '2345',
    })