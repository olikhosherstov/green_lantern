import csv


def get_users():
    with open('users.csv') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open('goods.csv') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods


def get_stores():
    with open('stores.csv') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
    return stores
