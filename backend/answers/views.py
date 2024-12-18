from answers import models
from sqlalchemy import orm
import api.models
import api.endpoints
import sqlalchemy
import api
import flask
import auth
import questions
import shared_library

answers_router = flask.Blueprint('answers_urls', 'answers')

class AnswersService(api.endpoints.AutoModelEndpoint):
    '''AnswersService
    
    Implements GET, PUT, DELETE methods in /api/v1/answers
    '''
    
    model: type[api.models.BaseModel] = models.Answer
    model_name: str = 'Answer'
    model_controller: api.models.ModelController = models.AnswerController
    
    visible_fields: list[str] = ['id', 'question_id', 'correct_answer']

class AnswersStaticService(api.endpoints.AutoEndpoint):
    '''AnswersStaticService
    
    Implements POST method for /api/v1/answers
    '''
    
    model: type[api.models.BaseModel] = models.Answer
    model_name: str = 'Answer'
    model_controller: api.models.ModelController = models.AnswerController
    
    visible_fields: list[str] = ['id', 'question_id', 'correct_answer']

    def post(self, **kwargs) -> flask.Response:
        try:
            if self._is_user_unauthorized('post'):
                return api.endpoints.errors.UnauthorizedError().make_error()
            
            question = ... # TODO
             
            model = self.model_controller.create(
                **(flask.request.json[self.model_name])
            )
            
            user = auth.AuthUser.get_current_user()
            self.access_controller.create_access_for_object(
                user, model, 
                # TODO
                default_access_for_everyone=self.default_everyone_permission,
            )
        except api.models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err),
            }), 400

'''
TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
Make sure that I haven't forgotten to create 
check_answer() method in question package and
I have completed AnswersStaticService (this is 
VERY important shit)
TODO TODO TODO TODO  TODO TODO TODO TODO TODO TODO
'''
