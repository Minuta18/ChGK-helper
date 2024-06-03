import flask
import os
import api

app = flask.Flask('ChKG-helper')

app.register_blueprint(api.views.router, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(
        host=os.environ.get('APP_HOST'),
        port=os.environ.get('APP_PORT'),
    )