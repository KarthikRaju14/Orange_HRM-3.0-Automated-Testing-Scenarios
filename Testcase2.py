from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# set up Firefox browser and navigate to the OrangeHRM 3.0 site login
class Test_case_2():
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "Invalid password"  # using invalid password as test data
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    # locate username and password input fields, and login button
    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()  
        
        # verify if error message is displayed
        if "Invalid credentials" in self.driver.page_source:
            print("Test Passed: Invalid employee login resulted in valid error message.")
        else:
            print("Test Failed: Invalid employee login did not result in valid error message.")
        

    # Method to start the webpage
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

s = Test_case_2()
s.login()
