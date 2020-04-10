from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such manager with user_id {user_id}'


class NoSuchStoreID(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
@app.errorhandler(NoSuchStoreID)
def store_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    goods_count = db.goods.add(request.json)
    return jsonify({'numbers of items created': goods_count}), 201


@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    goods = db.goods.get_goods()
    return jsonify(goods)


@app.route('/goods', methods=['PUT'])
def update_goods():
    db = inject.instance('DB')
    success, err = db.goods.update_goods(request.json)
    if err:
        return jsonify({'successfully updated': success, 'errors': {'no such id in goods': err}})
    else:
        return jsonify({'successfully updated': success})


@app.route('/stores', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    if db.users.get_user_by_id(request.json["manager_id"]):
        store_id = db.stores.add_store(request.json)
        return jsonify({'store_id': store_id}), 201


@app.route('/stores/<int:store_id>')
def get_store(store_id):
    db = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store)


@app.route('/stores/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    if db.users.get_user_by_id(request.json["manager_id"]):
        db.stores.update_store_by_id(store_id, request.json)
        return jsonify({'status': 'success'})
