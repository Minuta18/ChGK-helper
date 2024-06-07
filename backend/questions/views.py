from models import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask

questions_router = flask.Blueprint('questions_urls', 'questions')

@questions_router.route('/<int:question_id>', methods=['GET'])
def get_question(question_id: int):
    '''Gets a question with given id

    Returns the question by given id (int). If quesion not found returns
    a 404n error

    Args:
        question_id(int):question's id
    '''

    question = models.Question.get_question(question_id)
    if question is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find the question with id {question_id}',
        })
    return flask.jsonify({
        'error': False,
        'id': question_id,
        'text': question.text,
        'comment': question.comment,
    }), 200
