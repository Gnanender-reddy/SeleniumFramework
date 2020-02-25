"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has unit test frame work concept.
"""
import unittestpack
from selenium import webdriver

class searchengine(unittestpack.TestCase):


    def test_bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bing.com/")
        print(self.driver.title)
        self.driver.close()

if __name__ == '__main__':
    unittestpack.main()