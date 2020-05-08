from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,  nullable=False)
    password = db.Column(db.String, nullable=False)

class Goods(db.Model):
    __tablename__ = 'goods'

    good_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String, nullable=False)
    name = db.Column(db.String,  nullable=False)
    price = db.Column(db.Float, nullable=False)

class Stores(db.Model):
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String,  nullable=False)
    address = db.Column(db.String, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))