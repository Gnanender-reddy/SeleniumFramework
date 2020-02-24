import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_name(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        titlee=driver.title
        #assertEqual()
        #self.assertEqual("Google",titlee,"title page is not same") #third param is error message
        self.assertNotEqual("Google",titlee)
if __name__ == '__main__':
    unittest.main

