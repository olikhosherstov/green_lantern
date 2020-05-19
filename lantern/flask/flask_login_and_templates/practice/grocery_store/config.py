import os
from grocery_store.install import get_passwd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(ROOT_DIR, 'fixtures')


class Config:
    HOST = 'localhost'
    PORT = 5000
    SECRET_KEY = get_passwd('secret_key')
    PG_USER = "cursor"
    PG_PASSWORD = get_passwd('cursor_sqlalchemy_db')
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "cursor_sqlalchemy_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
