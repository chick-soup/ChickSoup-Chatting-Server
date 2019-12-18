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

    @jwt_required
    def post(self):
        roomId = get_jwt_identity()

        peoples = request.json['peoples']

        roomName = request.json['roomName']

        if peoples is None or \
            chattingRoomModel.objects(roomId = roomId).first():
            return {
                'status': 'ERROR',
                'message': 'WRONG REQUEST'
                   }, 409


        chattingRoomModel(
            roomID = roomId,
            roomName = roomName,
            peoples = peoples
        ).save()

        return {
            'status': 'OK',
            'message': 'CREATED THE CHATTING ROOM'
               }, 201