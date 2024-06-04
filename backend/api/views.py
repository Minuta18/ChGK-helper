import flask

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
