from grocery_store.db import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<id: {self.user_id}, name: {self.name}, email: {self.email}>'


class Good(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'<id: {self.good_id}, brand: {self.brand}, name: {self.name}, price: {self.price}>'


class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<id: {self.store_id}, name: {self.name}, city: {self.city}, address: {self.address}>'
