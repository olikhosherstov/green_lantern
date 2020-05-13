from grocery_store.app import make_app, make_db
from flask_script import Server, Manager
from grocery_store.config import Config

app = make_app()
db = make_db(app)

manager = Manager(app)
manager.add_command('runserver', Server(host=Config.HOST, port=Config.Port))
__all__ = ["app", "db"]
