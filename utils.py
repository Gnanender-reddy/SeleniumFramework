from selenium import webdriver

driver=webdriver.Chrome()
def normal(url):

    return driver.get(url)

def title():
    return driver.title