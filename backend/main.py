import flask
import users
import os
import api
import json
from werkzeug import exceptions

print(dir(api))

app = flask.Flask('ChKG-helper')

app.register_blueprint(api.views.router, url_prefix='/api/v1')
app.register_blueprint(users.views.users_router, url_prefix='/api/v1/users')
app.register_blueprint(api.swagger_router, url_prefix='/api/v1/docs')

@app.errorhandler(exceptions.HTTPException)
def handle_exception(error):
    '''Return JSON instead of HTML for HTTP errors.
    
    Handles HTTP exceptions to return JSON instead of HTML.

    Args:
        error: The exception
    '''
    response = error.get_response()
    response.data = json.dumps({
        'error': True,
        'detail': error.name,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    print(app.url_map)

    app.run(
        host=os.environ.get('APP_HOST'),
        port=os.environ.get('APP_PORT'),
    )
