from . import endpoint
from . import errors
import typing
import flask

class BaseApiEndpoint(endpoint.BaseEndpoint):
    '''JSONified base endpoint class
    
    Provides basic endpoint functionality
    '''
    
    def get(self, *args, **kwargs) -> typing.Any:
        '''Serves GET request'''
        return errors.MethodNotAllowedError().make_error()
    
    def post(self, *args, **kwargs) -> typing.Any:
        '''Serves POST request'''
        return errors.MethodNotAllowedError().make_error()
    
    def delete(self, *args, **kwargs) -> typing.Any:
        '''Serves DELETE request'''
        return errors.MethodNotAllowedError().make_error()
    
    def patch(self, *args, **kwargs) -> typing.Any:
        '''Serves PATCH request'''
        return errors.MethodNotAllowedError().make_error()
    
    def put(self, *args, **kwargs) -> typing.Any:
        '''Serves PUT request'''
        return errors.MethodNotAllowedError().make_error()
