import csv
import os

from grocery_store import app, db
from grocery_store.models import User, Goods, Stores
from grocery_store.config import FIXTURES_DIR
from sqlalchemy_utils import create_database, drop_database, database_exists

USERS_DIR = os.path.join(FIXTURES_DIR, 'users.csv')
GOODS_DIR = os.path.join(FIXTURES_DIR, 'goods.csv')
STORES_DIR = os.path.join(FIXTURES_DIR, 'stores.csv')

def get_users():
    with open(USERS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users

def get_goods():
    with open(GOODS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods

def get_stores():
    with open(STORES_DIR, 'r') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
    return stores


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        db.create_all()
        print('Data base created')

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(User(**user))

    goods = get_goods()
    for good in goods:
        db.session.add(Goods(**good))

    stores = get_stores()
    for store in stores:
        db.session.add(Stores(**store))

    db.session.commit()
    print('Data written in data_base succesfuly')
