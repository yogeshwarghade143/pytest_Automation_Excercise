import pytest                                             #there is no need to import pytest since we are not using any pytest methods in scripts like fixture markers etc.
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.readProperties import Readconfig           #not used yet
from PageObjects.signup_login import login
from PageObjects.SIgnUp_page import SignUp
from Utilities.logGenerator import loggen
import time

class Test_002_ENTER_AC_INFO():
    logger =loggen.log()
    baseUrl = Readconfig.Geturl()

    def test_enter_AC_info(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.signUP = SignUp(self.driver)  # object signUp
        self.lgn = login(self.driver)  # object created for class login provider driver init
        self.lgn.click_signup_login()
        self.lgn.enterNAme('yogesh')
        self.logger.info("*** name entered  ***")

        self.lgn.enterEmail('yog@gmail.com')
        self.logger.info("*** email entered  ***")

        self.logger.info("*** clicked sign up button  ***")
        self.lgn.clickSignUP()

        # ENTER ACCOUNT INFORMATION
        self.signUP.clickMr()
        self.logger.info("*** clicked TITLE  ***")

        self.signUP.password("yogesh")
        self.logger.info("*** ENTER PASSWORD  ***")

        self.signUP.dateDrpdwn("14")
        self.logger.info("*** ENTER DATE  ***")

        self.signUP.monthDrpdwn("10")
        self.logger.info("*** ENTER month  ***")

        self.signUP.yearDrpdwn("1995")
        self.logger.info("*** ENTER year  ***")


        #ENTER ADDRESS INFORMAION
        self.signUP.enterFirstName('yogesh')
        self.signUP.enterLasttName('warghade')
        self.signUP.enterCompany('errecsson')
        self.signUP.enterAddress1('jawhar')
        self.signUP.dropdownCountry('India')
        self.signUP.state('maharashtra')
        self.signUP.city('jawhar')
        self.signUP.zipcode(401666)
        self.signUP.mobileNo(555555555)
        self.signUP.createAccount()

        time.sleep(5)




