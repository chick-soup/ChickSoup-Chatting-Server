import os
import jwt
import requests
import time

from flask_socketio import Namespace, emit, join_room, leave_room

from app.models.chattingRoom import chattingRoomModel



class chattingNamespace(Namespace):
    def on_getChat(self, data):
        roomId = data['roomId']

        userId = str(jwt.decode(data['token'], os.getenv('SECRET_KEY'))['id'])

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            emit('chatData', {
                'status':'ERROR'
            })
            return None

        join_room(roomId)
        emit('chatData', chattingRoom['chatData'])


    def on_chatting(self, data):
        roomId = data['roomId']

        token = data['token']

        userId = str(jwt.decode(token, os.getenv('SECRET_KEY'))['id'])

        chat = data['chat']

        type = data['type']

        headers = {"Authorization": token}

        userName = requests.get('http://ec2-13-209-99-114.ap-northeast-2.compute.amazonaws.com:8080/users/my/profile',headers=headers).text

        chattingRoom = chattingRoomModel.objects(roomId = roomId).first()

        if not userId in chattingRoom['peoples'] or chattingRoom is None:
            emit('realTimeChat', {
                'ERROR':"이성진이 병신일때 일어나는 에러"
            })
            return None

        chattingRoom.chatData.append({
            'userId': userId,
            'name': userName,
            'chat': chat,
            'time': time.time(),
            'type': type
        })
        chattingRoom.save()

        emit('realTimeChat', {
            'roomId': roomId,
            'userId': userId,
            'chat': chat,
            'name': userName,
            'time': time.time(),
            'type' : type
        }, room = roomId)


    def on_quitChat(self, data):
        leave_room(data['roomId'])