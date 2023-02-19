from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

class Test_case_PIM_02():
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_module_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"

    # Method to login into the Portal using Python Selenium
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

    # Go to PIM module
    def go_to_pim_module(self):
        self.driver.find_element(By.XPATH, self.pim_module_xpath).click()

    # Edit an existing employee's information
    def edit_employee(self, employee_id, first_name, last_name):
        self.driver.find_element(By.ID, "empsearch_id").send_keys(employee_id)
        self.driver.find_element(By.ID, "searchBtn").click()
        self.driver.find_element(By.XPATH, "//a[text()='" + employee_id + "']").click()

        # Edit employee details and save
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "personal_txtEmpFirstName").clear()
        self.driver.find_element(By.ID, "personal_txtEmpFirstName").send_keys(first_name)
        self.driver.find_element(By.ID, "personal_txtEmpLastName").clear()
        self.driver.find_element(By.ID, "personal_txtEmpLastName").send_keys(last_name)
        self.driver.find_element(By.ID, "btnSave").click()

        # Verify successful message
        wait = WebDriverWait(self.driver, 5)
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message.success")))
        assert "Successfully Saved" in success_message.text

    # Close the browser
    def close_browser(self):
        self.driver.quit()

test = Test_case_PIM_02()
test.login()
test.go_to_pim_module()
test.edit_employee("0268", "maaya", "guptha")
test.close_browser()
