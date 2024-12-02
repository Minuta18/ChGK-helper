import flask
import flask.views
import typing

class BaseEndpoint(flask.views.View):
    '''Base endpoint class
    
    Provides basic endpoint functionality
    '''
    
    def dispatch_request(self, *args, **kwargs) -> typing.Any:
        '''Dispatches request'''
        req_method = flask.request.method
        if req_method == 'GET':
            return self.get(*args, **kwargs)
        elif req_method == 'POST':
            return self.post(*args, **kwargs)
        elif req_method == 'DELETE':
            return self.delete(*args, **kwargs)
        elif req_method == 'PATCH':
            return self.patch(*args, **kwargs)
        elif req_method == 'PUT': 
            return self.put(*args, **kwargs)
    
    def get(self, *args, **kwargs) -> typing.Any:
        '''Serves GET request'''
        return 'Method not allowed', 409
    
    def post(self, *args, **kwargs) -> typing.Any:
        '''Serves POST request'''
        return 'Method not allowed', 409
    
    def delete(self, *args, **kwargs) -> typing.Any:
        '''Serves DELETE request'''
        return 'Method not allowed', 409
    
    def patch(self, *args, **kwargs) -> typing.Any:
        '''Serves PATCH request'''
        return 'Method not allowed', 409
    
    def put(self, *args, **kwargs) -> typing.Any:
        '''Serves PUT request'''
        return 'Method not allowed', 409
    