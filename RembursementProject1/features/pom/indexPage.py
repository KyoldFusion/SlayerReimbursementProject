class Index:
    Home_link = "Home"
    Submit_Request = 'Submit Request'
    Submit_Request2 = 'SubmitREQ'
    Statistics = "Statistics"
    emp = "Requests"
    Notif_Drop = "navbarDropdownMenuLink"
    Log_out_drop = "logout"
    ham_drop = "hamb"
    ham_submit = "//*[@id='navbarSupportedContent']/ul/li[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def HomePage(self):
        self.driver.find_element_by_id(self.Home_link).click()

    def Submit_Quest(self):
        self.driver.find_element_by_link_text(self.Submit_Request).click()

    def Submit_Quest_2(self):
        self.driver.find_element_by_id(self.Submit_Request2).click()

    def Stats(self):
        self.driver.find_element_by_link_text(self.Statistics).click()

    def emp_req(self):
        self.driver.find_element_by_link_text(self.emp).click()

    def LogOut(self):
        self.driver.find_element_by_id(self.Notif_Drop).click()
        self.driver.find_element_by_id(self.Log_out_drop).click()

    def Hamburger(self):
        self.driver.find_element_by_id(self.ham_drop).click()

    def Submit_Ham(self):
        self.driver.find_element_by_xpath(self.ham_submit).click()