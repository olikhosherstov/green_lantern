import argparse
import csv
from random import randrange, choice
from typing import List
from time import sleep
import requests


class Fill_db:
    def __init__(self, url, count, table):
        #SetUp interface
        self.url = url
        self.count = count
        self.table = table
        #Fixtures for random user names
        if self.table == 'users':
            self.names: List = self.set_fixtures('names')
            self.surnames: List = self.set_fixtures('surnames')
            self.create_request(self.count)
        #Fixtures for random goods
        if self.table == 'goods':
            self.colors: List = self.set_fixtures('colors')
            self.clothes: List = self.set_fixtures('clothes')
            self.size: List = self.set_fixtures('size')
            self.create_request(1)
        #Fixtures for random stores
        if self.table == 'stores':
            self.colors: List = self.set_fixtures('colors')
            self.animals: List = self.set_fixtures('animals')
            self.create_request(self.count)

    def set_fixtures(self, data_name: str) -> list:
        with open(f'fixtures/{data_name}.csv') as fill:
            data_read = csv.reader(fill, delimiter=",")
            return [line[1] for line in data_read]

    def rand_feature(self, source1: List, source2: List, source3: List) -> str:
        return " ".join([choice(source1), choice(source2), choice(source3)]).strip()

    def create_request(self, count):
        i = 0
        flag = 0
        while i <= count:
            if self.table == 'users':
                request_data = self.make_user()
            elif self.table == 'goods':
                request_data = self.make_goods()
            else:
                request_data = self.make_store()
            try:
                resp = requests.post(self.url, json=request_data)
                if resp.status_code not in (200, 201):
                    print('Invalid table for fill or server error.')
                else:
                    i += 1
            except ConnectionRefusedError as e:
                print(type(e))
                print(f"Server {self.url} is disconnected. Try reconnect.")
                sleep(3)
                flag += 1
                if flag == 4:
                    raise ValueError(f'Requested server {self.url} is down.')
            print(f"Sended to server 1 requests.")
        print(f"Sended to server {i} requests.")

    def make_user(self):
        return {"name": self.rand_feature(self.names, self.surnames, [''])}

    def make_goods(self):
        post_goods = []
        for i in range(self.count):
            post_goods.append({
                               'name': self.rand_feature(self.colors,
                                                         self.clothes,
                                                         self.size),
                               'price': randrange(1, 100)
                               })
        return post_goods

    def make_store(self):
        return {
                'name': self.rand_feature(self.colors, self.animals, ['']),
                'location': 'Lviv',
                'manager_id': 1
                }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url for request")
    parser.add_argument("count", help="count of users", type=int)
    parser.add_argument("table", help="table for add, 'users', 'goods', 'stores'")
    args = parser.parse_args()
    filler = Fill_db(args.url+args.table, args.count, args.table)
