from flask import request, render_template, make_response, flash
from flask_restful import Resource, marshal
from grocery_store.models import Good
from grocery_store.database import db
from grocery_store.routes.marshal_structure import goods_structure


class Goods(Resource):
    def get(self, good_id=None):
        headers = {'Content-Type': 'text/html'}
        if good_id:
            good = Good.query.get(good_id)
            if good:
                goods = marshal(good, goods_structure)
                print(goods)
                return make_response(render_template('goods.html', title='GOODS', goods=goods),200,headers)
            flash(f"No such good with id: {good_id}")
            return make_response(render_template('goods.html', title=f"No such good with id: {good_id}"),404,headers)
        return make_response(render_template('goods.html', title='GOODS', goods=marshal(Good.query.all(), goods_structure)),200,headers)

    def post(self):
        good = Good(**request.json)
        db.session.add(good)
        db.session.commit()
        return f"Successfully added a new good {good}"

    def put(self, good_id):
        good = Good.query.get(good_id)
        good.name = request.json.get("name", good.name)
        good.brand = request.json.get("brand", good.brand)
        good.price = request.json.get("price", good.price)
        db.session.commit()
        return f"Successfully updated Good with id: {good_id}"

    def delete(self, good_id):
        good = Good.query.get(good_id)
        db.session.delete(good)
        db.session.commit()
        return f"Successfully deleted User with id: {good_id}"
