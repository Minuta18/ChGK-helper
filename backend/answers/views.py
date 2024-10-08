from answers import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask
import auth
import questions
import shared_library

answers_router = flask.Blueprint('answers_urls', 'answers')

@answers_router.route('/<answer_id>', methods=['GET'])
def get_answer(answer_id: int):
    '''Gets answer by an id.

    Returns answer by given id (int). If user not found returns 404 error.

    Args:
        answer_id(int): answer\'s id
    '''
    answer = models.Answer.get_answer(answer_id)

    print(answer)

    if answer is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find answer with id {answer_id}',
        }), 404
        
    question = questions.models.Question.get_question(answer.question_id)
    if question.visibility == questions.models.IsPublic.private:
        if auth.get_current_user().id != question.creator_id and \
            not auth.is_current_user_admin():
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 401)

    return flask.jsonify({
        'error': False,
        'id': answer_id,
        'question_id': answer.question_id,
        'correct_answer': answer.correct_answer,
    }), 200

@answers_router.route('/', methods=['GET'])
def get_answers():
    '''Gets multiple answers.

    Gets multiple answers from a specified page. Page is answers
    from n + 1 to n + number_of_answers.

    Args:
        start_answer_id (:obj:`int`, optional): Page. Default value is 1.
        number_of_answers (:obj:`int`, optional): 
        The number of users in one page.
            Default value is 20.
    '''

    start_answer_id = flask.request.args.get('start_answer_id', 20, type=int)
    number_of_answers = flask.request.args.get(
        'number_of_answers', 1, type=int
    )

    allow_private = auth.is_current_user_admin()

    answers = models.Answer.get_answers(
        start_answer_id, start_answer_id + number_of_answers, allow_private
    )

    return flask.jsonify({
        'error': False,
        'answers': [{
            'id': answer.id,
            'question_id': answer.question_id,
            'correct_answer': answer.correct_answer,
        } for answer in answers],
    }), 200

@answers_router.route('/', methods=['POST'])
def create_answer():
    '''Create answer.

    Create new answer.

    Args:
        question_id (:obj:`int`): Id the question on with
        it answer is answering.
        correct_answer (:obj:`str`): correct answer on question
    '''

    question_id = flask.request.json.get('question_id', None)
    correct_answer = flask.request.json.get('correct_answer', None)

    question = questions.models.Question.get_question(question_id)
    if question.visibility == questions.models.IsPublic.private:
        if auth.get_current_user().id != question.creator_id and \
            not auth.is_current_user_admin():
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 401)

    if question_id is None or correct_answer is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Programmer invalid',  
        }), 400

    try:
        answer = models.Answer.create_answer(
            question_id, correct_answer,
        )
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': str(e),
        }), 400

    return flask.jsonify({
        'error': False,
        'id': answer.id,
        'question_id': answer.question_id,
        'correct_answer': answer.correct_answer,
    }), 201

@answers_router.route('/<answer_id>', methods=['PUT'])
def update_answer(answer_id):
    '''Update existful answer

    Args:
        question_id (:obj:`int`): Id the question on with
        it answer is answering.
        correct_answer (:obj:`str`): correct answer on question
    '''

    question_id = flask.request.args.get('question_id', None)
    correct_answer = flask.request.json.get('correct_answer', None)

    try:
        answer = models.Answer.get_answer(answer_id).update_answer(
            question_id, 
            correct_answer
        )
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': str(e),
        }), 400
    
    question = questions.models.Question.get_question(answer.question_id)
    if question.visibility == questions.models.IsPublic.private:
        if auth.get_current_user().id != question.creator_id and \
            not auth.is_current_user_admin():
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 401)

    return flask.jsonify({
        'error': False,
        'id': answer.id,
        'question_id': answer.question_id,
        'correct_answer': answer.correct_answer,
    }), 200

@answers_router.route('/<number>', methods=['DELETE'])
def delete_answer(answer_id: int):
    '''Delete existful answer

    Args:
       id (:obj:`int`): Id of deleting answer.
    '''

    try:
        answer = models.Answer.get_answer(answer_id)
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': str(e),
        }), 400

    question = questions.models.Question.get_question(answer.question_id)
    if question.visibility == questions.models.IsPublic.private:
        if auth.get_current_user().id != question.creator_id and \
            not auth.is_current_user_admin():
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 401)

    models.Answer.delete_answer(answer_id)

    return flask.jsonify({
        'error': False
    }), 200

@answers_router.route('/<question_id>/check', methods=['POST'])
def check_answer(question_id: int):
    '''Check answer

    Args:
        question_id (:obj:`int`): Id of question.
        answer (:obj:`str`): answer which user give us.
    '''

    if flask.request.headers.get('Content-Type') != 'application/json':
        return flask.jsonify({
            'error': True,
            'message': 'Incorrect Content-Type header',
        }), 400

    session = api.db.get_session()
    try:
        correct_answer = session.scalars(sqlalchemy.select(
            models.Answer
        ).where(
            models.Answer.question_id == question_id
        )).all()[0]
    except IndexError:
        return flask.jsonify({
            'error': False,
            'answer_is_correct': False,
        })

    answer = flask.request.json.get('answer', '')

    cleaner = shared_library.strings.TextCleaner()
    cleaner.set_strategy(shared_library.strings.HardCleanStrategy())

    if cleaner.clean(correct_answer.correct_answer) == cleaner.clean(answer): 
        return flask.jsonify({
            'error': False,
            'answer_is_correct': True
        }), 200
    else:
        return flask.jsonify({
            'error': False,
            'answer_is_correct': False
        }), 200


@answers_router.route('/get/<question_id>', methods=['GET'])
def get_answer_by_question(question_id: int):
    '''Gets answer by an question_id.

    Returns answer by given question_id (int).
    If user not found returns 404 error.

    Args:
        question_id(int): question\'s id
    '''

    answer = models.Answer.get_answer(question_id)
    if answer is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find answer with id {question_id}',
        }), 404
    return flask.jsonify({
        'error': False,
        'id': answer.id,
        'question_id': question_id,
        'correct_answer': answer.correct_answer,
    }), 200
