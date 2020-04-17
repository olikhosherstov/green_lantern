import inject
from flask import request
from flask_restful import Resource


class Users(Resource):

    def post(self):
        db = inject.instance('DB')
        user_id = db.users.add(request.json)
        return {'user_id': user_id}, 201

    def get(self, user_id):
        db = inject.instance('DB')
        user = db.users.get_user_by_id(user_id)
        return user

    def put(self, user_id):
        db = inject.instance('DB')
        db.users.update_user_by_id(user_id, request.json)
        return {'status': 'success'}
