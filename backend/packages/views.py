import flask
import auth
import models
import users
import questions

packages_router = flask.Blueprint('packages_urls', 'packages')

@packages_router.route('/<int:package_id>', methods=['GET', ])
def get_package(package_id: int):
    '''Returns package
    
    Returns all details of a package and the list of questions in it. List of 
    questions requires pagination (e. g. you need to specify page and it's 
    size).

    Args:
        page_size (int): The number of questions in one page. Query argument.
            Default value is 20.
        page (int): Page. Query argument. Default value is 1.
        token (str, optional): The auth token.You can pass it using http header
            "authorization".
    '''

    page_size = flask.request.args.get('page_size', 20)
    page = flask.request.args.get('page', 1)

    if page_size > 100 or page_size < 0:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect page size',
        })
    if page < 1:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect page',
        })

    package = models.Package.get_package(package_id)

    needed_user = users.models.User.get_user(package.creator_id)
    real_user = auth.get_current_user()
    if not package.is_public == questions.models.IsPublic.public:
        if needed_user is None:
            if not auth.is_current_user_admin():
                return flask.jsonify({
                    'error': True,
                    'detail': 'Not enough permissions',
                }, 403)            
        if real_user is None:
            return flask.jsonify({
                'error': True,
                'detail': 'Unauthorized',
            }, 401)
        if real_user.id != needed_user.id:
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 403)

    return {
        'error': False,
        'info': {
            'title': package.name,
            'description': package.description,
            'creator_id': package.creator_id,
            'id': package.package_id,
            'hardness': package.hardness.value(),
            'visibility': package.visibility.value(),
            'is_tournament': package.get_is_tournament(),
            'question_count': package.get_question_count(),
        },
        'questions': [{
            'id': question.id,
            'text': question.text,
            'comment': question.comment,
            'visibility': question.visibility.value(),
            'creator_id': question.creator_id,    
        } for question in package.get_questions(
            limit=page_size, offset=((page - 1) * page_size),
        )]
    }

@packages_router.route('/', methods=['GET', ])
def get_packages():
    page = flask.request.args.get('page')

    if page < 1:
        return flask.jsonify({
            'error': True,
            'detail': 'incorrect page',
        })

    page_size = flask.request.args.get('page_size')

    if page_size < 1 or page_size > 100:
        return flask.jsonify({
            'error': True,
            'detail': 'incorrect page_size',
        })

    by_user = flask.request.args.get('by_user')
    sort_by = flask.request.args.get('sort_by')
    reverse_sort = flask.request.args.get('reverse_sort')
    reverse_sort = reverse_sort == 'True'

    if sort_by == 'id':
        sort_by = models.SortBy.model_id
    elif sort_by == 'time':
        sort_by = models.SortBy.created_time
    else:
        return flask.jsonify({
            'error': True,
            'detail': 'sort_by must be "id" or "time"',
        }, 400)    

    user = auth.get_current_user()
    if user is None:
        if by_user is not None:
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permission',
            }, 403)
        else:
            user_packages = models.Packages.get_packages(
                limit=page_size, offset=(page - 1) * page_size,
                sort_by=sort_by, reverse_sort=reverse_sort,
            )
    else:
        if by_user is None:
            user_packages = models.Packages.get_packages(
                limit=page_size, offset=(page - 1) * page_size,
                sort_by=sort_by, reverse_sort=reverse_sort,
            )
        if by_user != user.id and \
            user.permissions != users.models.UserPermissions.ADMIN:
            return flask.jsonify({
                'error': True,
                'detail': 'Not enough permissions',
            }, 403)
        else:
            user_packages = models.Packages.get_packages(
                limit=page_size, offset=(page - 1) * page_size,
                sort_by=sort_by, reverse_sort=reverse_sort,
                by_user=by_user,
            )
    return flask.jsonify({
        'error': False,
        'packages': [
            {
                'title': package.name,
                'description': package.description,
                'creator_id': package.creator_id,
                'id': package.package_id,
                'hardness': package.hardness.value(),
                'visibility': package.visibility.value(),
                'is_tournament': package.get_is_tournament(),
                'question_count': package.get_question_count(),
            }
        for package in user_packages],
    })

@packages_router('/', methods=['POST', ])
def create_package():
    user = auth.get_current_user()
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Not authenticated',
        }, 401)    
    
    name = flask.request.json.get('name')
    description = flask.request.json.get('description')
    hardness = flask.request.json.get('hardness')

    if name is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Param \"name\" is required',
        }, 400)
