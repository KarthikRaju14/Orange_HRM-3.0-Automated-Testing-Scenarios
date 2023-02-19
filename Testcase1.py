from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# set up Firefox browser and navigate to the OrangeHRM 3.0 site login
class Test_case_1():
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
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

    # Method to start the webpage
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Example usage
if __name__ == '__Dashboard__':
    o = dashboard()
    success = o.login()
    if success:
        print('User is logged in successfully')
    else:
        print('Failed to log in')
    o.quit()


s =Test_case_1 ()

s.login()

   