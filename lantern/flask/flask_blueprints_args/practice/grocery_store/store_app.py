import inject
from flask import Flask
<<<<<<< HEAD

=======
>>>>>>> 2961b5c07e4406801602b17195f5a205e9d146f4
from flask_restful import Api

from errors import NoSuchUserError, my_error_handler, NoSuchStoreError
from fake_storage import FakeStorage
from routes.stores import Store
<<<<<<< HEAD
from routes.users import Users
from routes.goods import Goods
=======
>>>>>>> 2961b5c07e4406801602b17195f5a205e9d146f4


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


def make_app():
    # configure our database
    inject.clear_and_configure(configure)

    app = Flask(__name__)
    # API
    api = Api(app)
<<<<<<< HEAD
    api.add_resource(Store, "/stores", "/stores/<int:store_id>")
    api.add_resource(Users, "/users", "/users/<int:user_id>")
    api.add_resource(Goods, "/goods")
    # register blueprints and error handlers
=======
    api.add_resource(Store, "/store", "/store/<int:store_id>")
    # register blueprints and error handlers
    app.register_blueprint(users_bl)
    app.register_blueprint(goods_bl)

>>>>>>> 2961b5c07e4406801602b17195f5a205e9d146f4

    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreError, my_error_handler)
    return app
