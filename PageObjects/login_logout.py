from selenium import webdriver
from selenium.webdriver.common.by import By


class LogIn_LogOut:
    textBox_email_name = "email"
    textBox_password_name = "password"
    button_logIn_xpath = "//*[@id='form']/div/div/div[1]/div/form/button"
    button_logOut_xpath = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self,email):
        self.driver.find_element(By.NAME, self.textBox_email_name).clear()
        self.driver.find_element(By.NAME, self.textBox_email_name).send_keys('yog@gmail.com')

    def enterpassword(self,password):
        self.driver.find_element(By.NAME, self.textBox_password_name).clear()
        self.driver.find_element(By.NAME, self.textBox_password_name).send_keys('yogesh@12345')

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.button_logIn_xpath).click()

    def clickLogOut(self):
        self.driver.find_element(By.XPATH, self.button_logOut_xpath).click()
