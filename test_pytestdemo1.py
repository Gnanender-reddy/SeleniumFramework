import pytest

@pytest.fixture() #this fixture method is executed before every method
def setup():
    print("once before every method")

def testmethod1(setup):
    print("this is method1")

def testmethod2(setup):
    print("this is method 2")