import random

from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.chattingRoom import chattingRoomModel


api = Api(Blueprint(__name__, __name__))

@api.resource('/room')
class roomManagement(Resource):
    @jwt_required
    def get(self):
        UserId = get_jwt_identity()

        res = []

        for chattingRoom in chattingRoomModel.objects().all():
            if UserId in chattingRoom['peoples']:
                res.append({
                    'roomId':chattingRoom['roomId'],
                    'roomName':chattingRoom['roomName']
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

        peoples = request.json['peoples']

        roomName = request.json['roomName']

        if peoples is None or \
            chattingRoomModel.objects(roomId = roomId).first():
            return {
                'status': 'ERROR',
                'message': 'WRONG REQUEST',
                'roomId': roomId
                   }, 409


        chattingRoomModel(
            roomId = roomId,
            roomName = roomName,
            peoples = peoples
        ).save()

        return {
            'status': 'OK',
            'message': 'CREATED THE CHATTING ROOM'
               }, 201