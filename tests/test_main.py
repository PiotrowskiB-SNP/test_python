import pytest


@pytest.fixture
def int_fixture() -> int:
    return 1


def test_always_possitive():
    assert True


def test_something_positive():
    assert True


def test_use_fixture(int_fixture):
    assert int_fixture + 15 == 16
