import pytest                                             #there is no need to import pytest since we are not using any pytest methods in scripts like fixture markers etc.
from selenium import webdriver
from selenium.webdriver.common.by import By

# from Utilities.readProperties import Readconfig           #not used yet
from PageObjects.signup_login import login
from PageObjects.SIgnUp_page import SignUp
from Utilities.logGenerator import loggen
import time


class Test_001_homepage:
    logger =loggen.log()

    def test_homepage_visibility(self,setup):

        self.logger.info("***   start dirver   ***")
        self.driver = setup
        time.sleep(3)

        self.logger.info("***   OPEN url    ***")
        self.driver.get("https://www.automationexercise.com/")     #always give proper url try to copy it from browser itself sometimes it shows error
        time.sleep(3)
        act_title=self.driver.title

        if act_title == "Automation Exercise":                     #always check for '==' sign or code may fail
            self.logger.info("***   TITLE IS MATCHED   ***")
            assert True
        else:
            self.logger.info("***   TITLE DOES NOT MATCH   ***")
            assert False
    #


    def test_signup_login(self,setup):
        self.driver = setup
        self.driver.get("https://www.automationexercise.com/")
        self.signUP = SignUp(self.driver)                                #object signUp
        self.lgn = login(self.driver)                                    #object created for class login provider driver init
        self.lgn.click_signup_login()                                    #always copy method name from pageobject otherwise it gives error
        time.sleep(3)
        self.logger.info("***   successfull  ***")
        signup_user = self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2').text

        if signup_user=="New User Signup!":
            assert True
            self.logger.info("***   New User Signup! is visible   ***")

        else:
            self.logger.info("***   New User Signup! is not visible   ***")     #after "false" we cant put anything
            assert False

        # enter name and emaiil and press sign up button
        self.lgn.enterNAme('yogesh')
        self.logger.info("*** name entered  ***")

        self.lgn.enterEmail('yog1@gmail.com')
        self.logger.info("*** email entered  ***")

        self.logger.info("*** clicked sign up button  ***")
        self.lgn.clickSignUP()

        #ENTER ACCOUNT INFORMATION
        self.signUP.clickMr()
        self.signUP.password("yogesh")
        self.signUP.dateDrpdwn("14")
        self.signUP.monthDrpdwn("10")
        self.signUP.yearDrpdwn("1995")




