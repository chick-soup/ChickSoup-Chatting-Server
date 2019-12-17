from flask import Blueprint
from flask_restful import Api, Resource


api = Api(Blueprint(__name__, __name__))

@api.resource('/room')
class roomManagement(Resource):
    def get(self):
        return 'Hello'

    def post(self):
        return 'POST'