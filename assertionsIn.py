"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has
assertions concept.
"""
import unittest
class Test(unittest.TestCase):
    def test_name(self):
        list=['python','cat','snake']
        self.assertNotIn('python',list)
if __name__ == '__main__':
    unittest.main()