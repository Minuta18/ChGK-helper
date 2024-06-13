from auth import views
from flask_httpauth import HTTPTokenAuth
from auth import models

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    try:
        user = models.Token.get_user_by_token(token)
    except ValueError:
        return None

    return user
