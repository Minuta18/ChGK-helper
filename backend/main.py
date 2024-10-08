import flask_cors
import flask
import users
import os
import api
import json
import questions
import answers
import auth
import packages
from werkzeug import exceptions

app = flask.Flask('ChKG-helper')
cors = flask_cors.CORS(app)

app.register_blueprint(api.views.router, url_prefix='/api/v1')
app.register_blueprint(users.views.users_router, url_prefix='/api/v1/users')
app.register_blueprint(api.swagger_router, url_prefix='/api/v1/docs')
app.register_blueprint(auth.views.auth_router, url_prefix='/api/v1/auth')
app.register_blueprint(
    packages.views.packages_router, url_prefix='/api/v1/packages'
)
app.register_blueprint(
    questions.views.questions_router, url_prefix='/api/v1/questions'
)
app.register_blueprint(
    answers.views.answers_router, url_prefix='/api/v1/answer'
)

app.url_map.strict_slashes = False

@app.errorhandler(exceptions.HTTPException)
def handle_exception(error):
    '''Return JSON instead of HTML for HTTP errors.

    Handles HTTP exceptions to return JSON instead of HTML.S

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
    api.db.create_tables()

    print(app.url_map)

    app.run(
        # host=os.environ.get('APP_HOST'),
        host='0.0.0.0',        
        port=os.environ.get('APP_PORT'),
    )
