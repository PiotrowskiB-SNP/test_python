import pytest
from src import some_other_helper


@pytest.fixture
def int_fixture() -> int:
    return 1


def test_always_possitive():
    assert True


def test_something_positive():
    assert True


def test_use_fixture(int_fixture: int):
    assert int_fixture + 15 == 16


def test_nothing():
    assert 1 == 1


def test_helper():
    assert some_other_helper(5, 5)
