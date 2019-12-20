from time import time

from flask_socketio import Namespace, emit, join_room, leave_room

from app.models.chattingRoom import chattingRoomModel


class chattingNamespace(Namespace):
    def on_getChat(self, data):
        roomId = data['roomId']

        userId = data['userId']

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            return None

        join_room(roomId)
        emit('chatData', chattingRoom['chatData'])

    def on_chatting(self, data):
        roomId = data['roomId']

        userId = data['userId']

        chat = data['chat']

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            return None

        chattingRoom.chatData.append({
            'userId': userId,
            'name': 'UCHAN',
            'chat': chat,
            'time': time()
        })

        chattingRoom.save()

        emit('realTimeChat', {
            'roomId': roomId,
            'userId': userId,
            'chatData': chat,
            'name': 'TESTNAME',
            'time': time()
        }, room = roomId)