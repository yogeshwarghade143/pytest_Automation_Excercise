import time

from selenium import webdriver
from PageObjects.login_logout import LogIn_LogOut
from PageObjects.signup_login import login
from Utilities.logGenerator import loggen
from Utilities.readProperties import Readconfig

class Test_login_logOut:
    logger = loggen.log()
    baseUrl = Readconfig.Geturl()

    def test_logIn(self,setup):
        self.logger.info("setup driver")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.logger.info("** clicked url **")
        print(self.driver.title)
        self.logger.info("** print title **")
        self.lgn_lgout = login(self.driver)
        self.logger.info("** object of login created **")
        self.lgn_lgout.click_signup_login()
        self.logger.info("** signUp/login clicked **")
        self.lgn = LogIn_LogOut(self.driver)
        self.logger.info("** object for logIN and logOut created **")
        self.lgn.enterEmail('yog@gmail.com')
        self.logger.info("** enter username **")
        self.lgn.enterpassword('yogesh@12345')
        self.logger.info("** enter password **")
        self.lgn.clickLogIn()
        time.sleep(3)
        act_title = self.driver.title
        print(self.driver.title)
        if act_title == 'Automation Exercise':
            assert True
            self.logger.info("** test log is success **")

        else:
            self.logger.info("** test login failed **")
            assert False

        self.driver.close()

    # Test logOut

    def test_LogOut(self,setup):
        self.driver = setup
        self.logger.info("** enter url **")
        self.driver.get(self.baseUrl)
        self.lgn_lgout = login(self.driver)
        self.lgn_lgout.click_signup_login()
        self.lgn = LogIn_LogOut(self.driver)
        self.logger.info("** enter username **")
        self.lgn.enterEmail('yog@gmail.com')
        self.logger.info("** enter pasaword **")
        self.lgn.enterpassword('yogesh@12345')
        self.logger.info("** click log in button**")
        self.lgn.clickLogIn()
        print(self.driver.title)
        self.logger.info("** click log out button **")
        self.lgn.clickLogOut()
        print(self.driver.title)

        self.driver.quite()












