from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.logGenerator import loggen
from PageObjects.home import Homepage


class Test_testCase_varification:
    baseUrl = Readconfig.Geturl()
    logger = loggen.log()


    def test_testcase_varification(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.hp = Homepage(self.driver)
        self.hp.clicKTestCase_btn()
        self.driver.quit()
