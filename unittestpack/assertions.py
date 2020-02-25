"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has
unittest concept.
"""

import unittestpack
from selenium import webdriver
class Test(unittestpack.TestCase):
    def test_name(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        titlee=driver.title
        #assertEqual()
        #self.assertEqual("Google",titlee,"title page is not same") #third param is error message
        self.assertNotEqual("Google",titlee)
if __name__ == '__main__':
    unittestpack.main

