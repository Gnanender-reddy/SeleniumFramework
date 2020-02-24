import unittest
class Apptesting(unittest.TestCase):

    def test_search(self):
        print("this is your search ")

    def test_advancedsearch(self):
        print("this is advanced search")

    def test_prepaidrecharge(self):
        print("this prepaid")
    @unittest.skipIf(1==1,"if 1==1")
    def test_postpaidrecharge(self):
        print("this is postpaid")
    @unittest.skip("i want to skip") #skipping test with reason
    def test_loginbygmail(self):
        print("this is gmail")
    @unittest.SkipTest
    def test_loginbytwiter(self):
        print("this is twitter")

if __name__ == '__main__':
    unittest.main