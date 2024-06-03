import flask
import os

app = flask.Flask('ChKG-helper')

if __name__ == '__main__':
    app.run(
        host=os.environ.get('APP_HOST'),
        port=os.environ.get('APP_PORT'),
    )