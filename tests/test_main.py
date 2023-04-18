from src import complicated_script
import pytest


@pytest.fixture
def int_fixture() -> int:
    return 1


def test_always_possitive():
    assert True


def test_something_positive():
    assert False


def test_use_fixture(int_fixture: int):
    assert int_fixture + 15 == 16


def test_complicated_script():
    assert len(complicated_script()) > 0


def test_nothing():
    assert 1 == 1
