import inject
from flask import request
from flask_restful import Resource


class Goods(Resource):

    def post(self):
        db = inject.instance('DB')
        number_of_created_goods = db.goods.add_many(request.json)
        return {'number of items created': number_of_created_goods}, 201

    def get(self):
        db = inject.instance('DB')
        return db.goods.get_all()

    def put(self):
        db = inject.instance('DB')
        success, err = db.goods.update_goods(request.json)
        if err:
            return {'successfully updated': success, 'errors': {'no such id in goods': err}}
        else:
            return {'successfully updated': success}
