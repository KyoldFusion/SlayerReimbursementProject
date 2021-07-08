from selenium.webdriver.common.keys import Keys

class Login:
    id_field = "username"
    pw_field = "password"
    login_button = "login"

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element_by_name(self.id_field).send_keys("hotboy")
        self.driver.find_element_by_name(self.pw_field).send_keys("gutted")

    def fill_form_emp(self):
        self.driver.find_element_by_id(self.id_field).send_keys("heal")
        self.driver.find_element_by_id(self.pw_field).send_keys("everybody")

    def find_submit(self):
        self.driver.find_element_by_id(self.login_button).click()

