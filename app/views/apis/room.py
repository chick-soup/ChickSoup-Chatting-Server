import os
import jwt
import random

from flask import Blueprint, request
from flask_restful import Api, Resource

from app.models.chattingRoom import chattingRoomModel


api = Api(Blueprint(__name__, __name__))

@api.resource('/room')
class roomManagement(Resource):
    def get(self):
        try:
            UserId = str(jwt.decode(request.headers['Authorization'], os.getenv('SECRET_KEY'))['id'])
        except:
            return {
                "status":"token has expired"
            }, 403

        res = []

        for chattingRoom in chattingRoomModel.objects().all():
            if UserId in chattingRoom['people']:
                res.append({
                    'roomId':chattingRoom['roomId'],
                    'roomName':chattingRoom['roomName'],
                    'people': chattingRoom['people']
                })
        return {
            'status': 'OK',
            'rooms': res
        }, 200

    def post(self):
        while True:
            flag = True
            roomId = str(random.randrange(11111,99999))

            for room in chattingRoomModel.objects().all():
                if roomId == room['roomId']:
                    flag = False
                    break

            if flag:
                break
        try:
            id = str(jwt.decode(request.headers['Authorization'], os.getenv('SECRET_KEY'))['id'])
        except:
            return {
                       "status": "token has expired"
                   }, 403

        people = request.json['people']
        roomName = request.json['roomName']

        people.append(id)

        if people is None or \
            chattingRoomModel.objects(roomId = roomId).first():
            return {
                'status': 'ERROR',
                'message': 'WRONG REQUEST',
                'roomId': roomId
                   }, 409


        chattingRoomModel(
            roomId = roomId,
            roomName = roomName,
            people = people
        ).save()

        return {
            'status': 'OK',
            'message': 'CREATED THE CHATTING ROOM'
               }, 201

    def put(self):
        roomId = request.json['roomId']

        roomName = request.json['roomName']

        chattingRoom = chattingRoomModel.objects(roomId=roomId).first()

        chattingRoom.update(
            roomName = roomName
        )

        chattingRoom.save()

        return 201

    def delete(self):
        try:
            id = str(jwt.decode(request.headers['Authorization'], os.getenv('SECRET_KEY'))['id'])
        except:
            return {
                       "status": "token has expired"
                   }, 403
        roomId = request.json['roomId']

        chattingRoom = chattingRoomModel.objects(roomId=roomId).first90

        people = chattingRoom['people']

        try:
            people.remove(id)
        except:
            return {
                "status": "Bad request"
            }, 403

        chattingRoom.update(
            people = people
        )

        chattingRoom.save()

        return {
            "status": "OK"
        }, 200