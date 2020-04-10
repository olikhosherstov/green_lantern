from itertools import count
from store_app import NoSuchUserError, NoSuchStoreID


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = VirtualGoods()
        self._stores = VirtualStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class VirtualGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def get_rec_count(self):
        return len(self._goods)

    def add(self, goods):
        i = 0
        for post in goods:
            goods_id = next(self._id_counter)
            post["id"] = goods_id
            self._goods[goods_id] = post
            i += 1
        return i

    def get_goods(self):
        return [self._goods[i] for i in range(1, len(self._goods) + 1)]

    def update_goods(self, goods):
        success = 0
        err = []
        for post in goods:
            good_id = post["id"]
            if good_id in self._goods:
                self._goods[good_id] = post
                success += 1
            else:
                err.append(good_id)
        return success, err


class VirtualStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add_store(self, store):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreID(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreID(store_id)
