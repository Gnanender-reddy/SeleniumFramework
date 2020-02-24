import pytest

@pytest.fixture() #this fixture method is executed before every method
def setup():
    print("once before every method execution")
    yield
    print("once after every method execution")

def test_loginByEmail(setup):
    print("this is method1")

def test_loginByFacebook(setup):
    print("this is method 2")