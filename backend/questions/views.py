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
        'question':
            'id': question_id,
            'text': question.text,
            'comment': question.comment,
    }), 200

@questions_router.route('/', methods=['GET'])
def get_questions():
    '''Gets multiple questions
    
    Gets multiple question from a specified page. A page is questions
    from n + 1 to n + page size

    Args:
        page_size (:obj:`int`, optional): The number of questions in one page
            Default value is 20.
        page (:obj:`int`, optional)
    '''
    page_size = flask.request.args.get('page_size', 20, type=int)
    page = flask.request.args.get('page', 1, type=int)

    return flask.jsonify({
        'error': False,
        'questions': [{
            'id': question.id,
            'text': question.text,
            'comment': question.comment,
        }]
    })
