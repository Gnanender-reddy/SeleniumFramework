"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python selenium basics which has
pytest concept.
"""

from selenium import webdriver
import pytest


class TestOrangeApp:

    @pytest.yield_fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title=="OrangeHRM"


    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"

