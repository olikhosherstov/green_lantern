import argparse
import csv
from random import randrange

import requests


def data_sets(data_name: str):
    with open(f'data/{data_name}.csv') as fill:
        data_read = csv.reader(fill, delimiter=",")
        return {int(line[0]): line[1] for line in data_read}


def add_users(url: str, count_user):
    names = data_sets("names")
    surnames = data_sets("surnames")
    rand_name = lambda x_name, y_surname: " ".join([x_name.get(randrange(1, 65), 1),
                                                    y_surname.get(randrange(1, 277), 1)])
    try:
        if requests.post(url, json={'name': rand_name(names, surnames)}).status_code == 201:
            for i in range(count_user):
                # Can been 17728 different combinations
                data = rand_name(names, surnames)
                requests.post(url, json={'name': data})
                print(data)
            print(f"Sended to server {i + 1} requests.")
        else:
            print("Invalid table.")
    except ConnectionRefusedError:
        print(f"Server {url} is not connected. Try another URL.")


def add_goods(url: str, count_goods):
    colors = data_sets("colors")
    clothes = data_sets("clothes")
    size = data_sets("size")
    post_goods = []
    rand_name = lambda x, y, z: " ".join([x.get(randrange(1, 151), 1),
                              y.get(randrange(1, 78), 1),
                              z.get(randrange(1, 9), 1)]
                             )
    for i in range(count_goods):
        # Can been 106002 different combinations
        post_goods.append({'name': rand_name(colors, clothes, size), 'price': randrange(1, 100)})
    try:
        resp = requests.post(url, json=post_goods)
        if resp.status_code == 201:
            print(f"Sended to server serial data with {resp.json()['numbers of items created']} goods.")
        else:
            print("Invalid table.")
    except ConnectionRefusedError:
        print(f"Server {url} is not connected. Try another URL.")


def add_store(url: str, count_stores):
    colors = data_sets("colors")
    animals = data_sets("animals")
    rand_name = lambda x, y: " ".join([x.get(randrange(1, 151), 1), y.get(randrange(1, 51), 1)])
    try:
        resp = requests.post(url, json={'name': rand_name(colors, animals),
                                        'location': 'Lviv', 'manager_id': 1})
        if resp.status_code == 201:
            for i in range(count_stores):
                # Can been 7500 different combinations
                post_store = {'name': rand_name(colors, animals), 'location': 'Lviv', 'manager_id': 1}
                requests.post(url, json=post_store)
                print(post_store)
            print(f"Sended to server {i + 1} requests.")
        else:
            print("Invalid table or users not added.")
    except ConnectionRefusedError:
        print(f"Server {url} is not connected. Try another URL.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url for request")
    parser.add_argument("count", help="count of users", type=int)
    parser.add_argument("table", help="table for add, USERS, GOODS, STORES")
    args = parser.parse_args()
    if args.table == "users":
        add_users(args.url + "/users", args.count)
    elif args.table == "goods":
        add_goods(args.url + "/goods", args.count)
    elif args.table == "stores":
        add_store(args.url + "/stores", args.count)
