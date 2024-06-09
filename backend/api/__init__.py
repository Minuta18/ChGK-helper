import shared_library
import flask_swagger_ui
import re
from api import views

db = shared_library.DB_connection('sqlite:///./app.db')
orm_base = db.get_base()

def load_regex(filename: str):
    with open(filename, 'r') as f:
        return re.compile(f.read())
    
SWAGGER_URL = '/api/v1/docs'
API_URL = '/api/v1/swagger' # I have no idea what does it do, I just copied 
                            # from guide: https://habr.com/ru/companies/ivi/
                            # articles/542204/ 

swagger_router = flask_swagger_ui.get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={
        'app_name': 'ChGK-helper',
    }, 
)