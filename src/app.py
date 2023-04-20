import flask
import uuid
import random
from .helpers import some_other_helper, helper_fun


app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid4())


@app.route('/')
def go_home_param():
    return 'Home sweet home!!!!'


@app.route('/something')
def go_somewhere():
    return 'Somewhere -> ' + str(helper_fun(flask.session))\
        + ' <- here. \t And something else: ' + \
        str(some_other_helper(0, random.randint(-2, 2)))


@app.route('/something/<anything>')
def go_somewhere_with_param(anything):
    return f'A something like this: {flask.escape(anything)}'


@app.route('/user(<int:user_id>)')
def go_user(user_id):
    return f'User {flask.escape(user_id)}'


@app.route('/user')
def show_users():
    users = ['Bartosz', 'Patric', 'Christian']
    return flask.render_template('users.html', users=users)


@app.route('/user(<username>)')
def show_user(username: str):
    return f'Site for user {flask.escape(username)}'


# for browser request will fail - browsers use GET, but for postman
# or something simillar it would return error 418 - I'm a teapot
@app.route('/err', methods=['POST'])
def navigate_error():
    return flask.Response(status=418)


if __name__ == '__main__':
    # execute app on localhost - for local testing only
    app.run(host='0.0.0.0')
