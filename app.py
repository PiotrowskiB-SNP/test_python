# import flask_cors
import flask
import uuid
import random
import main


COUNTER_NAME = 'counter'

app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid4())


@app.route('/')
def go_home_param():
    return f'Home sweet home!!!!'


def helper_fun() -> int:
    # save and read data from browser cache
    counter_value = flask.session.get(COUNTER_NAME, 0) + 1
    flask.session[COUNTER_NAME] = counter_value
    return counter_value


def some_other_helper(x: int, y: int) -> bool:
    return x == y


@app.route('/something')
def go_somewhere():
    return 'Somewhere -> ' + str(helper_fun()) + ' <- here. \t And something else: ' + str(some_other_helper(0, random.randint(-2, 2)))


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
    return f'Site for user {flask.escape(uslername)}'


# for browser request will fail - browsers use GET, but for postman or something simillar it would return error 418 - I'm a teapot
@app.route('/err', methods=['POST'])
def navigate_error():
    return flask.Response(status=418)


def int_returner() -> int:
    return 37


if __name__ == '__main__':

    app.run(host='0.0.0.0')  # execute app on localhost
