import flask
import json
from werkzeug import exceptions

router = flask.Blueprint('urls', 'api')

@router.route('/', methods=['GET'])
def health_check():
    '''Health-check endpoint.

    Returns the current status of the server (usually it's \"running\"). It
    can be used to like this:

    ```bash
    curl https://<api_domain>/api/v1/health_check
    ```

    Args:
        No arguments

    Returns:
        flask.Response: Response object
    '''

    return flask.jsonify({
        'status': 'working',
    }), 200

with open('./swagger.json', 'r') as f:
    swagger_file = f.read()

@router.route('/swagger', methods=['GET'])
def get_swagger_json():
    '''Returns a swagger.json file'''
    response = flask.Response(content_type='application/json', status=200)
    response.set_data(swagger_file)
    return response
