from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# set up Firefox browser and navigate to the OrangeHRM 3.0 site login
class Test_case_PIM_01():
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

    # Method to add new employee
    def add_new_employee(self):
        self.driver.find_element(by=By.ID, value="menu_pim_viewPimModule").click()
        self.driver.find_element(by=By.ID, value="btnAdd").click()

        # fill in employee details
        self.driver.find_element(by=By.ID, value="firstName").send_keys("Nate")
        self.driver.find_element(by=By.ID, value="MiddleName").send_keys("Howard")
        self.driver.find_element(by=By.ID, value="lastName").send_keys("Jacobs")
        self.driver.find_element(by=By.ID, value="employeeId").send_keys("EMP0001")
        self.driver.find_element(by=By.ID, value="photofile").send_keys("D:\\jacob.jpg")
        self.driver.find_element(by=By.ID, value="btnSave").click()

        # verify successful employee addition
        success_message = self.driver.find_element(by=By.XPATH, value="//div[@class='message success fadable']")
        assert success_message.text == "Successfully Saved", "Employee addition failed."

# test the PIM_01 test case
s = Test_case_PIM_01()
s.login()






