from selenium import webdriver
from selenium.webdriver.common.by import By

class login:
    linktext_signup_login = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    textbox_newUserSignUp_Name = '//*[@id="form"]/div/div/div[3]/div/form/input[2]'
    textbox_newUserSignUp_email = '//*[@id="form"]/div/div/div[3]/div/form/input[3]'
    button_signUP = '//*[@id="form"]/div/div/div[3]/div/form/button'

    def __init__(self,driver):
        self.driver = driver

    def click_signup_login(self):
        self.driver.find_element(By.XPATH, self.linktext_signup_login).click()

    def enterNAme(self,name):
        self.driver.find_element(By.XPATH,self.textbox_newUserSignUp_Name ).send_keys(name)

    def enterEmail(self,email):
        self.driver.find_element(By.XPATH,self.textbox_newUserSignUp_email ).send_keys(email)

    def clickSignUP(self):
        self.driver.find_element(By.XPATH,self.button_signUP ).click()

