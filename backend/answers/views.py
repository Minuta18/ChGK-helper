from answers import models
from questions import models as question_models
import api.models
import api.endpoints
import api
import flask
import auth

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
            
            question_id = flask.request.json[self.model_name]['question_id']
            question = question_models.QuestionController.get_by_id(question_id)
            
            model = self.model_controller.create(
                **(flask.request.json[self.model_name])
            )
            
            user = auth.AuthUser.get_current_user()
            self.access_controller.create_access_for_object(
                user, model, 
                default_access_for_everyone =
                    self.access_controller.get_access_level(question, None),   
            )
            
            return flask.jsonify({
                'error': False,
                'answer': self._model_as_dict(model),    
            }), 201
        except api.models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err),
            }), 400
        except IndexError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err),
            }), 400

answers_router.add_url_rule(
    '/<int:model_id>', view_func=AnswersService.as_view('answers_service'),
    methods=['GET', 'PUT', 'DELETE', ],
)
   
answers_router.add_url_rule(
    '/', view_func=AnswersStaticService.as_view('answers_static_service'),
    methods=['POST', ],
)
