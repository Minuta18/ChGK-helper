import flask

class HttpError:
    '''HttpError
    
    Sometimes (very often) you need to write something like this:
    
    ```
    return flask.jsonify({
        'error': True,
        'detail': 'Not enough permission',
    }), 403
    ```
    
    Now you can write this:
    
    ```
    return HttpError(
        detail='Not enough permission', error_code=403).make_error()
    ```
    '''
    
    def __init__(self, 
        detail: str | None = None,
        error_code: int = 400,
    ):
        self.detail = detail
        self.error_code = error_code
        
    def make_error(self) -> flask.Response:
        '''Represents error as http request'''
        
        if self.detail is None:
            return flask.jsonify({
                'error': True,
            }), self.error_code
        return flask.jsonify({
            'error': True,
            'detail': self.detail,
        }), self.error_code
        
class NotEnoughPermissionsError(HttpError):
    def __init__(self, 
        detail: str | None = 'Not enough permissions',
        error_code: int = 403,
    ):
        super().__init__(detail=detail, error_code=error_code)
        
class UnauthorizedError(HttpError):
    def __init__(self, 
        detail: str | None = 'Unauthorized',
        error_code: int = 401,
    ):
        super().__init__(detail=detail, error_code=error_code)
        
class NotFoundError(HttpError):
    def __init__(self, 
        detail: str | None = 'Item not found',
        error_code: int = 404,
    ):
        super().__init__(detail=detail, error_code=error_code)
        
class MethodNotAllowedError(HttpError):
    def __init__(self, 
        detail: str | None = 'Method not allowed',
        error_code: int = 409,
    ):
        super().__init__(detail=detail, error_code=error_code)
