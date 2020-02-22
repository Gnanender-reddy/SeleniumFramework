"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has mouse drag and drop actions concept.
"""
import unittest

from selenium import webdriver
class searchengine(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

    def test_kuch(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bing.com/")
        print(self.driver.title)
        self.driver.close()





if __name__ == '__main__':
    unittest.main()