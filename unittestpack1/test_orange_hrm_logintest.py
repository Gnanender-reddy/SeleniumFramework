"""

@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has
unitest html reports concept.
"""



from selenium import webdriver
import unittest
import HtmlTestRunner
class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homepage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"web page title not matchingt")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title,"webpage title not working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("test completed")
if __name__ == '__main__':
    #unittest.main() to run unit test we need this main function
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/admin1/PycharmProjects/pythonseleniumframework/reports'))