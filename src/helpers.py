COUNTER_NAME = 'counter'


def int_returner() -> int:
    return 37


def some_other_helper(x: int, y: int) -> bool:
    return x - 1 == y - 1


def helper_fun(flask_session) -> int:
    # save and read data from browser cache
    counter_value = flask_session.get(COUNTER_NAME, 0) + 1
    flask_session.session[COUNTER_NAME] = counter_value
    return counter_value
