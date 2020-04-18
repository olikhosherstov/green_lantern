import inject
from flask import request
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=False, type=str)


class Users(Resource):

    def post(self):
        db = inject.instance('DB')
        user_id = db.users.add(request.json)
        return {'user_id': user_id}, 201

    def get(self, user_id=None):
        db = inject.instance('DB')
        if user_id is not None:
            user = db.users.get_user_by_id(user_id)
            return user, 200
        else:
            args = parser.parse_args()
            name = args['name']
            user_id, user = db.users.get_user_by_name(name)
            return {'user_id': user_id, 'name': user}, 200

    def put(self, user_id):
        db = inject.instance('DB')
        db.users.update_user_by_id(user_id, request.json)
        return {'status': 'success'}
