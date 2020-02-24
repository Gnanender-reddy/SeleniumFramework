import pytest

@pytest.yield_fixture()
def setup():
    print("once before every method") #this statement is executed before every method execution.
    yield
    print("once after every method")#this statement is executed after every method execution.

def testmethod1(setup):
    print("this is method1")

def testmethod2(setup):
    print("this is method 2")