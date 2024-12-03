from . import endpoint
import typing
import flask

class BaseApiEndpoint(endpoint.BaseEndpoint):
    '''JSONified base endpoint class
    
    Provides basic endpoint functionality
    '''
    
    def get(self, *args, **kwargs) -> typing.Any:
        '''Serves GET request'''
        return flask.jsonify({
            'error': True,
            'detail': 'Method not allowed'
        }), 409
    
    def post(self, *args, **kwargs) -> typing.Any:
        '''Serves POST request'''
        return flask.jsonify({
            'error': True,
            'detail': 'Method not allowed'
        }), 409
    
    def delete(self, *args, **kwargs) -> typing.Any:
        '''Serves DELETE request'''
        return flask.jsonify({
            'error': True,
            'detail': 'Method not allowed'
        }), 409
    
    def patch(self, *args, **kwargs) -> typing.Any:
        '''Serves PATCH request'''
        return flask.jsonify({
            'error': True,
            'detail': 'Method not allowed'
        }), 409
    
    def put(self, *args, **kwargs) -> typing.Any:
        '''Serves PUT request'''
        return flask.jsonify({
            'error': True,
            'detail': 'Method not allowed'
        }), 409
