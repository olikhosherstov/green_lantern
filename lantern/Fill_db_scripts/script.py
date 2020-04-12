import csv, requests, argparse
from random import randrange


def add_users(url:str, count_user):
    with open('data/names.csv') as fill:
        name_read = csv.reader(fill, delimiter=",")
        names = {int(line[0]): line[1] for line in name_read}
    with open('data/surnames.csv') as fill:
        reading = csv.reader(fill, delimiter=",")
        surnames = {int(line[0]): line[1] for line in reading}
    for i in range(count_user):
        # Can been 17728 different combinations
        rand_name = " ".join([names.get(randrange(1,65),1), surnames.get(randrange(1,277),1)])
        post_user = {'name': rand_name}
        requests.post(url, json=post_user)
        print(rand_name)
    print(f"Added {i} users.")


def add_goods(url:str, count_goods):
    with open('data/colors.csv') as fill:
        post_read = csv.reader(fill, delimiter=",")
        colors = {int(line[0]): line[1] for line in post_read}
    with open('data/clothes.csv') as fill:
        post_read = csv.reader(fill, delimiter=",")
        clothes = {int(line[0]): line[1] for line in post_read}
    with open('data/size.csv') as fill:
        post_read = csv.reader(fill, delimiter=",")
        size = {int(line[0]): line[1] for line in post_read}
    post_goods = []
    for i in range(count_goods):
        # Can been 106002 different combinations
        rand_name = " ".join([colors.get(randrange(1,151),1),
                              clothes.get(randrange(1,78),1),
                              size.get(randrange(1,9),1)]
                             )
        post_goods.append({'name': rand_name, 'price': randrange(1,100)})
    print(post_goods)
    resp = requests.post(url, json=post_goods)
    print(f"Added {resp.json()['numbers of items created']} goods.")


def add_store(url:str, count_stores):
    with open('data/colors.csv') as fill:
        post_read = csv.reader(fill, delimiter=",")
        colors = {int(line[0]): line[1] for line in post_read}
    with open('data/animals.csv') as fill:
        post_read = csv.reader(fill, delimiter=",")
        animals = {int(line[0]): line[1] for line in post_read}
    for i in range(count_stores):
        # Can been 7500 different combinations
        rand_name = " ".join([colors.get(randrange(1,151),1), animals.get(randrange(1,51),1)])
        post_store = {'name': rand_name, 'location': 'Lviv', 'manager_id': 1}
        resp = requests.post(url, json=post_store)
        print(post_store)
        print(resp.json)
    print(f"Added {i} stores.")


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
