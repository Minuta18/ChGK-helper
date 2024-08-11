from packages import models
from auth import models
from user import models
from questions import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask
import base64

packages_router = flask.Blueprint('packages_urls', 'packages')

@packages_router.route('/<id>', methods=['GET', ])
def get_answers_in_package(id):
    page_size = flask.request.args.get('page_size', None)
    page = flask.request.args.get('page', None)

    token = flask.request.headers.get('Authorization', '')

    package = models.Packages.get_package(id)

    user = auth.models.Token.get_user_by_token(token.removeprefix('Bearer '))

    if user.id == package.user_id or user.permission == UserPermissions.ADMIN:
        if package == None:
            return flask.jsonify({
                'error': True,
                'detail': 'No package',
            }), 400
        else:
            all_questions = models.PackagesToQuestions.get_questions_by_package_id(id)
            questions = []
            for i in range(page_size):
                questions.append(all_questions[page + i])
            return flask.jsonify({
                'error': False,
                'info': {
                    'title': package.name,
                    'description': package.description,
                    'created_by': user.nickname,
                    "creator_id": package.user_id,
                    "id": package.id,
                    "question_count": all_questions.len(),
                },
                'questions': [{
                    'id': question.question_id,
                    'text': models.Question.get_question(question.question_id).text,
                    'comment': models.Question.get_question(question.question_id).comment,
                } for question in questions],
            }), 200
    else:
        return flask.jsonify({
            'error': True,
            'detail': 'No permission',
        }), 403

@packages_router.route('/', methods=['GET', ])
def get_packages(id):
    page_size = flask.request.args.get('page_size', None)
    page = flask.request.args.get('page', None)

    token = flask.request.headers.get('Authorization', '')

    package = models.Packages.get_package(id)

    user = auth.models.Token.get_user_by_token(token.removeprefix('Bearer '))

    if user.id == package.user_id or user.permission == UserPermissions.ADMIN:
        if package == None:
            return flask.jsonify({
                'error': True,
                'detail': 'No package',
            }), 400
        else:
            all_questions = models.PackagesToQuestions.get_questions_by_package_id(id)
            questions = []
            for i in range(page_size):
                questions.append(all_questions[page + i])
            return flask.jsonify({
                'error': False,
                'info': {
                    'title': package.name,
                    'description': package.description,
                    'created_by': user.nickname,
                    "creator_id": package.user_id,
                    "id": package.id,
                    "question_count": all_questions.len(),
                },
                'questions': [{
                    'id': question.question_id,
                    'text': models.Question.get_question(question.question_id).text,
                    'comment': models.Question.get_question(question.question_id).comment,
                } for question in questions],
            }), 200
    else:
        return flask.jsonify({
            'error': True,
            'detail': 'No permission',
        }), 403
