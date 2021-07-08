from selenium.webdriver.common.keys import Keys

class RequestPage:

    all = "all"
    pending = "pending"
    R_ID = "reimburse"
    Purpose = "purpose"
    approve = "approved_reim"

    def __init__(self, driver):
        self.driver = driver

    def show_all(self):
        self.driver.find_element_by_id(self.pending).click()

    def approve_rem(self):
        self.driver.find_element_by_id(self.R_ID).send_keys("26")
        self.driver.find_element_by_id(self.Purpose).send_keys("Auto approval")
        self.driver.find_element_by_class_name(self.approve).click()