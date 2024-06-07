from api import views
import shared_library
import re

db = shared_library.DB_connection('sqlite://./app.db')
orm_base = db.get_base()

def load_regex(filename: str):
    with open(filename, 'r') as f:
        return re.compile(f.read())
    