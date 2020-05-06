import inject
from flask import Blueprint, request, jsonify

goods_bl = Blueprint("goods", __name__)


@goods_bl.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    number_of_created_goods = db.goods.add_many(request.json)
    return jsonify({'number of items created': number_of_created_goods}), 201


@goods_bl.route('/goods')
def get_goods():
    db = inject.instance('DB')
    return jsonify(db.goods.get_all())

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

