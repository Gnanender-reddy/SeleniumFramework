"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has skipping test concept.
"""


import unittestpack
class Apptesting(unittestpack.TestCase):

    def test_search(self):
        print("this is your search ")

    def test_advancedsearch(self):
        print("this is advanced search")

    def test_prepaidrecharge(self):
        print("this prepaid")
    @unittestpack.skipIf(1 == 1, "if 1==1")
    def test_postpaidrecharge(self):
        print("this is postpaid")
    @unittestpack.skip("i want to skip") #skipping test with reason
    def test_loginbygmail(self):
        print("this is gmail")
    @unittestpack.SkipTest
    def test_loginbytwiter(self):
        print("this is twitter")

if __name__ == '__main__':
    unittestpack.main