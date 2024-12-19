from shared_library import strings
import api.endpoints
from questions import models
import api
import flask
import auth

questions_router = flask.Blueprint('questions_urls', 'questions')

class QuestionService(api.endpoints.AutoModelEndpoint):
    '''Question Service
    
    Implements GET, PUT, DELETE methods in /api/v1/questions
    '''
    
    model: type[api.models.BaseModel] = models.Question
    model_name: str = 'Question'
    model_controller: api.models.ModelController = models.QuestionController
    
    visible_fields: list[str] = ['id', 'creator_id', 'text', 'comment']

class QuestionStaticService(api.endpoints.AutoEndpoint):
    '''Question static service
    
    Implements POST method for /api/v1/questions
    '''
    
    model: type[api.models.BaseModel] = models.Question
    model_name: str = 'Question'
    model_controller: api.models.ModelController = models.QuestionController
    
    visible_fields: list[str] = ['id', 'creator_id', 'text', 'comment']

    def post(self, **kwargs) -> flask.Response:
        try:
            if self._id_user_unauthorized('post'):
                return api.endpoints.errors.UnauthorizedError().make_error()
            
            user = auth.AuthUser.get_current_user()
            create_kwargs = flask.request.json[self.model_name]
            create_kwargs['creator_id'] = user.id
            model = self.model_controller.create(**create_kwargs)
            
            self.access_controller.create_access_for_object(
                model, user,
            )
            
            return flask.jsonify({
                'error': False,
                'question': self._model_as_dict(model)
            }), 201
        except api.models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err),
            }), 400

class QuestionCheckingService(api.endpoints.BaseApiEndpoint):
    '''Question checking service
    
    Service to check if answer is correct 
    '''

    model: type[api.models.BaseModel] = models.Question
    model_name: str = 'Question'
    model_controller: api.models.ModelController = models.QuestionController
    
    def get(self, question_id: int, **kwargs) -> flask.Response:
        try:
            question = self.model_controller.get_by_id(question_id)
             
            cleaner = strings.TextCleaner()
            cleaner.set_strategy(strings.HardCleanStrategy())
            checker = strings.AnswerChecker()
            
            for answer in question.answers:
                if checker.check_answer(
                    flask.request.json['answer'], 
                    answer.correct_answer
                ):
                    return flask.jsonify({
                        'error': False,
                        'is_answer_correct': True
                    }), 200
                    
            return flask.jsonify({'error': False, 'is_answer_correct': False})
        except api.models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': 'question not found',
            }), 404
        except IndexError as error:
            return flask.jsonify({
                'error': True,
                'detail': str(error)
            })

questions_router.add_url_rule(
    '/<int:model_id>', view_func=QuestionService.as_view('questions_service'),
    methods=['GET', 'PUT', 'DELETE', ],
)

# questions_router.add_url_rule(
#     '/<int:model_id>', view_func=QuestionService.as_view('questions_service'),
#     methods=['GET', 'PUT', 'DELETE', ],
# )

# questions_router.add_url_rule(
#     '/<int:model_id>', view_func=QuestionService.as_view('questions_service'),
#     methods=['GET', 'PUT', 'DELETE', ],
# )
