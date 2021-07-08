from selenium.webdriver.common.keys import Keys


class SubmitPage:

    eco = "economy"
    purpose = "purpose"
    manager_id = "manager_id"
    option = 1

    def __init__(self, driver):
        self.driver = driver

    def input_request(self):
        self.driver.find_element_by_id(self.eco).send_keys("1000")
        self.driver.find_element_by_id(self.purpose).send_keys("automation test", Keys.RETURN)