"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has
assertions concept.
"""

import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_name(self):
        driver=webdriver.Chrome()
        driver.get("https://google.com")
        tittle=driver.title
        #self.assertTrue(tittle,"Google")
        self.assertFalse(tittle=="Google12")
if __name__ == '__main__':
    unittest.main()
