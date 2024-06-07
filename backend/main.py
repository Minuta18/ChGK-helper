import flask
import os
import api
import questions

app = flask.Flask('ChKG-helper')

app.register_blueprint(api.views.router, url_prefix='/api/v1')
api.register_blueprint(questions.views.questions_router, url_prefix='/api/v1/questions')

if __name__ == '__main__':
    app.run(
        host=os.environ.get('APP_HOST'),
        port=os.environ.get('APP_PORT'),
    )
