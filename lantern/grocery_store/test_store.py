import inject
import json
import pytest

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Johny Week'}
        )
        assert resp.json == {'user_id': 2}

    @pytest.mark.parametrize(
        "flask_request, status_code, flask_response",
        (
            (1, 200, {'name': 'John Doe'}),
            (2, 404, {'error': 'No such manager with user_id 2'})
        )
    )
    def test_successful_get_user(self, flask_request, status_code, flask_response):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.get(f'/users/{flask_request}')
        assert resp.status_code == status_code
        assert resp.json == flask_response

    @pytest.mark.parametrize(
        "flask_request, status_code, flask_response",
        (
            (1, 200, {'status': 'success'}),
            (2, 404, {'error': 'No such manager with user_id 2'})
        )
    )
    def test_update_user(self, flask_request, status_code, flask_response):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.put(
            f'/users/{flask_request}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == status_code
        assert resp.json == flask_response


class TestGoods(Initializer):
    def test_create_goods(self):
        with open('test_data/goods_adding.json') as fill:
            resp = self.client.post(
                '/goods',
                json=json.load(fill)
            )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 10}
        resp = self.client.post(
            '/goods',
            json=[{"name": "Pepsi, 1.5L", "price": 23.5}]
        )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 1}

    def test_get_goods(self):
        with open('test_data/goods_adding.json') as fill:
            self.client.post(
                '/goods',
                json=json.load(fill)
            )
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        with open('test_data/goods_test.json') as test_data:
            assert resp.json == json.load(test_data)

    def test_update_goods(self):
        with open('test_data/goods_adding.json') as fill:
            self.client.post(
                '/goods',
                json=json.load(fill)
            )
        with open('test_data/goods_update.json') as upd:
            resp = self.client.put(
                '/goods',
                json=json.load(upd)
            )
        assert resp.status_code == 200
        assert resp.json == {'successfully updated': 5, 'errors': {'no such id in goods': [12, 13, 14]}}


def fill_managers():
    with open('test_data/managers.json') as managers:
        for person in json.load(managers):
            with app.test_client() as client:
                client.post(
                    '/users',
                    json=person
                )


class TestStore(Initializer):

    @pytest.mark.parametrize(
        "flask_request, status_code, flask_response",
        (
            ({'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}, 201, {'store_id': 1}),
            ({'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 20}, 404,
             {'error': 'No such manager with user_id 20'})
        )
    )
    def test_create_new_store(self, flask_request, status_code, flask_response):
        fill_managers()
        resp = self.client.post(
            '/stores',
            json=flask_request
        )
        assert resp.status_code == status_code
        assert resp.json == flask_response

    @pytest.mark.parametrize(
        "flask_request, status_code, flask_response",
        (
            (1, 200, {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}),
            (2, 404, {'error': 'No such store_id 2'})
        )
    )
    def test_get_store(self, flask_request, status_code, flask_response):
        fill_managers()
        self.client.post(
            '/stores',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        resp = self.client.get(f'/stores/{flask_request}')
        assert resp.status_code == status_code
        assert resp.json == flask_response

    @pytest.mark.parametrize(
        "request_json, flask_request, status_code, flask_response",
        (
            ({'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}, 1, 200, {'status': 'success'}),
            ({'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}, 2, 404, {'error': 'No such store_id 2'}),
            ({'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 20}, 1, 404,
             {'error': 'No such manager with user_id 20'})
        )
    )
    def test_update_store(self, request_json, flask_request, status_code, flask_response):
        fill_managers()
        self.client.post(
            '/stores',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        resp = self.client.put(
            f'/stores/{flask_request}',
            json=request_json
        )
        assert resp.status_code == status_code
        assert resp.json == flask_response
