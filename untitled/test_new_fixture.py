import pytest


@pytest.fixture(scope='module')
def module():
    print("module function")
    return 10


@pytest.fixture(scope='session')
def session_fun():
    print("session function")
    return 11


def test_first_case(module, session_fun):
    assert session_fun == 11
    assert module == 10


def test_second_case(module, session_fun):
    assert session_fun == 11
    assert module == 10
