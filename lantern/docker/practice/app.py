from flask import Flask
from sqlalchemy_utils import create_database, drop_database, database_exists
from config import Config
from populate_data import get_users, get_goods, get_stores
from models import db, Users, Goods, Stores

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print("Database is exists.")
    else:
        print(f"Database does not exist.{db.engine.url}")
        create_database(db.engine.url)
        db.create_all()
        print((f"Database created on {db.engine.url}"))

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(Users(**user))
    db.session.commit()
    print('Data writen in table "Users" succesfuly')

with app.app_context():
    goods = get_goods()
    for good in goods:
        db.session.add(Goods(**good))
    db.session.commit()
    print('Data writen in table "Goods" succesfuly')

with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Stores(**store))
    db.session.commit()
    print('Data writen in table "Stores" succesfuly')