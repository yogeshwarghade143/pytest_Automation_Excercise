from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage:
    botton_testcase_xpath = '//*[@id="slider-carousel"]/div/div[1]/div[1]/a[1]/button'

    def __init__(self,driver):
        self.driver = driver

    def clicKTestCase_btn(self):
        self.driver.find_element(By.XPATH, self.botton_testcase_xpath).click()