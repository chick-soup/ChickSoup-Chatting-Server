import os
import jwt
import requests
import time

from flask_socketio import Namespace, emit, join_room, leave_room

from app.models.chattingRoom import chattingRoomModel



class chattingNamespace(Namespace):
    reader = []

    def on_getChat(self, data):
        roomId = data['roomId']

        userId = jwt.decode(data['token'], os.getenv('SECRET_KEY'))['id']

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            emit('chatData', {
                'status':'ERROR'
            })
            return None

        join_room(roomId)
        self.reader.append(userId)
        emit('chatData', chattingRoom['chatData'])

    def on_chatting(self, data):
        roomId = data['roomId']

        token = data['token']

        userId = jwt.decode(token, os.getenv('SECRET_KEY'))['id']

        chat = data['chat']

        headers = {"Authorization": token}

        userName = requests.get('http://ec2-13-209-99-114.ap-northeast-2.compute.amazonaws.com:8080/users/my/profile',headers=headers).text

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            return None

        for readers in chattingRoom['chatData']['read']:
            for human in self.reader:
                readers.append(human)

        chattingRoom.chatData.append({
            'userId': userId,
            'name': userName,
            'chat': chat,
            'time': time.time(),
            'read': readers
        })
        chattingRoom.save()

        emit('realTimeChat', {
            'roomId': roomId,
            'userId': userId,
            'chatData': chat,
            'name': userName,
            'time': time.time()
        }, room = roomId)


    def on_quitChat(self, data):
        leave_room(data['roomId'])