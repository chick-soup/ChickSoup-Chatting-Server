import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("[-] CONNECTED")

@sio.event
def disconnect():
    print("[-] DISCONNECTED")

@sio.on('notice')
def notice(msg):
    print(msg)

@sio.on('get')
def chatting(msg):
    print(msg)

sio.connect('http://10.156.147.139:5555')

while True:
    msg = input()
    sio.emit('get', {
        "user":"migsking",
        "room":"12345",
        "msg":msg
    })