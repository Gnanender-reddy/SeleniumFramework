

import pytest

@pytest.fixture() #this fixture method is executed before every method
def setup():
    print("once before every method execution")
    yield
    print("once after every method execution")

def test_signupByEmail(setup):
    print("this is method1")

def test_signupByFacebook(setup):
    print("this is method 2")
# pytest -v -s /home/admin1/PycharmProjects/pythonseleniumframework/pytestpack/ --> command for executing all test cases in one package