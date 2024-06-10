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
        }), 404
    return flask.jsonify({
        'error': False,
        'question': {
            'id': question_id,
            'text': question.text,
            'comment': question.comment,
        }
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

    if (page_size < 1 or page_size > 100):
        return flask.jsonify({
            'error': True,
            'detail': f'Invalid page size: { page_size }'
        }), 400

    page = flask.request.args.get('page', 1, type=int)

    if (page < 1):
        return flask.jsonify({
            'error': True,
            'detail': f'Invalid page: { page }',
        }), 400

    return flask.jsonify({
        'error': False,
        'questions': [{
            'id': question.id,
            'text': question.text,
            'comment': question.comment,
        } for question in models.User.get_users(
            from_id=((page - 1) * page_size + 1), to_id=(page * page_size)
        )]
    }), 200

@questions_router.route('/', methods=['POST'])
def create_user():
    '''Creates new question.

    Creates new question.

    Args:
        text (str): Text of the new question
        comment (str): Comment to the question
    '''

    if flask.request.headers.get('Content-Type') != 'application/json':
        return flask.jsonify({
            'error': True,
            'message': 'Incorrect Content-Type header',
        })
    text = flask.request.json.get('text', '')
    comment = flask.request.json.get('text', '')

    try:
        question = models.Question.create_user(text, comment)
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': str(e),
        }), 400

    return flask.jsonify({
        'error': False,
        'id': question.id,
        'text': question.text,
        'comment': question.comment,
    }), 201

@questions_router.route('/<int:user_id>', methods=['PUT'])
def edit_question(question_id: int):
    '''Edits question by given id.

    Edits question by given id.

    Args:
        text (:obj:`str`, optional): New text of the question.
        comment (:obj:`str`, optional): New comment of the new question.
    '''

    text = flask.request.args.get('text', None, type=str)
    comment = flask.request.args.get('comment', None, type=str)

    question = models.Question.get_question(question_id)

    if question is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Question not found'
        }), 404

    if text is not None:
        question.text = text

    if comment is not None:
        question.comment = comment

    session = api.db.get_session()
    session.add(question)
    try:
        session.commit()
        return flask.jsonify({
            'error': False,
            'id': question.id,
            'text': question.text,
            'comment': question.comment,
        }), 200
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        return flask.jsonify({
            'error': True,
            'detail': 'question already exists',
        }), 400

@questions_router.route('/<int:user_id>', methods=['DELETE'])
def delete_question(question_id: int):
    '''Deletes question by given id'''
    try:
        models.Question.delete_question(question_id)
        return flask.jsonify({
            'error': False,
        }), 200
    except ValueError:
        return flask.jsonify({
            'error': True,
            'detail': 'Question not found',
        }), 404
