from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_case_PIM_03():
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
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value="username").send_keys(self.username)
        self.driver.find_element(by=By.NAME, value="password").send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    # Method to start the webpage
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Go to PIM module
    def go_to_pim_module(self):
        self.driver.find_element(By.XPATH, self.pim_module_xpath).click()

    # Delete an existing employee's information
    def delete_employee(self, employee_id):
        self.driver.find_element(By.ID, "empsearch_id").send_keys(employee_id)
        self.driver.find_element(By.ID, "searchBtn").click()
        self.driver.find_element(By.XPATH, "//a[text()='" + employee_id + "']").click()

        # Click on delete button and confirm the deletion
        self.driver.find_element(By.ID, "btnDelete").click()
        wait = WebDriverWait(self.driver, 3)
        confirm_delete_button = wait.until(EC.visibility_of_element_located((By.ID, "dialogDeleteBtn")))
        confirm_delete_button.click()

        # Verify successful message
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message.success")))
        assert "Successfully Deleted" in success_message.text

    # Close the browser
    def close_browser(self):
        self.driver.quit()

s = Test_case_PIM_03()
s.login()
s.go_to_pim_module()
s.delete_employee("0268")
s.close_browser()
