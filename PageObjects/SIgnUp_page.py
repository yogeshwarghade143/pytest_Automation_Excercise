from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignUp:
    #ACCOUNT INFORMATION
    id_Rbtn_Gender1 = "id_gender1"
    id_Rbtn_Gender2 = "id_gender2"
    textbox_id_password = "password"
    drpDwn_id_date = "days"
    drpDwn_id_month = "months"
    drpDwn_id_year = "years"
    checkBox_Xpath_settler = '//*[@id="form"]/div/div/div/div[1]/form/div[6]/label'
    checkBox_id_offer = "optin"

    #ADDRESS INFORMATION
    textbox_id_firstname = 'first_name'
    textbox_id_lastname = 'last_name'
    textbox_id_company = 'company'
    textbox_id_address1 = 'address1'
    textbox_id_address2 = 'address2'
    dropdown_country = 'country'
    textbox_id_state = 'state'
    textbox_id_city = 'city'
    textbox_id_zipcode = 'zipcode'
    textbox_id_mobile_number = 'mobile_number'
    btn_xpath_createAccount = '//*[@id="form"]/div/div/div/div[1]/form/button'

    def __init__(self,driver):
        self.driver = driver

    def clickMr(self):
        self.driver.find_element(By.ID, self.id_Rbtn_Gender1).click()

    def clickMrs(self):
        self.driver.find_element(By.ID, self.id_Rbtn_Gender2).click()

    def password(self,password):
        self.driver.find_element(By.ID, self.textbox_id_password).send_keys("yogesh@12345")

    def dateDrpdwn(self,date):
        date_element = self.driver.find_element(By.ID, self.drpDwn_id_date)
        drpdwnDate = Select(date_element)
        drpdwnDate.select_by_visible_text(date)

    def monthDrpdwn(self,month):
        month_element = self.driver.find_element(By.ID, self.drpDwn_id_month)
        drpdwn = Select(month_element)
        drpdwn.select_by_index(month)

    def yearDrpdwn(self,year):
        years_element = self.driver.find_element(By.ID, self.drpDwn_id_year)
        drpdwn = Select(years_element)
        drpdwn.select_by_visible_text(year)

    def signUPNewSettler(self):
        self.driver.find_element(By.XPATH, self.checkBox_Xpath_settler).click()

    def recieveOffers(self):
        self.driver.find_element(By.XPATH, self.checkBox_id_offer).click()


    def enterFirstName(self,firstname):
        self.driver.find_element(By.ID,self.textbox_id_firstname ).send_keys(firstname)

    def enterLasttName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_id_lastname).send_keys(lastname)

    def enterCompany(self, company):
        self.driver.find_element(By.ID, self.textbox_id_lastname).send_keys(company)


    def enterAddress1(self, Address1):
        self.driver.find_element(By.ID, self.textbox_id_address1).send_keys(Address1)

    def enterAddress2(self, Address2):
        self.driver.find_element(By.ID, self.textbox_id_address2).send_keys(Address2)

    def dropdownCountry(self, country):

        ele =  self.driver.find_element(By.ID, self.dropdown_country)

        dropdown = Select(ele)
        dropdown.select_by_visible_text(country)

    def state(self,state):
        self.driver.find_element(By.ID,self.textbox_id_state ).send_keys(state)

    def city(self, city):
        self.driver.find_element(By.ID, self.textbox_id_city).send_keys(city)

    def zipcode(self, zipcode):
        self.driver.find_element(By.ID, self.textbox_id_zipcode).send_keys(zipcode)

    def mobileNo(self, number):
        self.driver.find_element(By.ID, self.textbox_id_mobile_number).send_keys(number)

    def createAccount(self):
        self.driver.find_element(By.XPATH, self.btn_xpath_createAccount).click()











