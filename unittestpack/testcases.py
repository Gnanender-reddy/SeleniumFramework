"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has unit test frame work concept with setup and tear down methods.
"""

import unittestpack

def setUpModule():#This setup module is executed once before module(class) execution.
    print("This is setup module")

def tearDownModule():#This teardown module is executed once after module(class) execution.
    print("this is tear down module")

class AppTesting(unittestpack.TestCase):
    @classmethod
    def setUp(self):
        """
        This method will be executed before every test methods execution.
        """
        print("This is setup method")

    @classmethod
    def tearDown(self):
        """
        This method will be executed after every test methods execution.
        """
        print("This is tear down method")

    @classmethod
    def setUpClass(cls) :
        """
        This method will be executed once before all test methods execution.

        """
        print("This is setup class")

    @classmethod
    def tearDownClass(cls):
        """
        This method will be executed once after all test methods execution.

        """
        print("this is tear down class")

    def test_search(self):
        print("This is search test")

    def test_advancedSearch(self):
            print("This is advanced search")

    def test_prepaidrecharge(self):
            print("This is prepaid search")

    def test_postpaidsearch(self):
        print("This is post paid search")

if __name__ == '__main__':
    unittestpack.main