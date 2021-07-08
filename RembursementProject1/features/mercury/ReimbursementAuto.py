import time

from selenium import webdriver
from features.pom.loginPage import Login
from features.pom.indexPage import Index
from features.pom.requestsPage import RequestPage
from features.pom.SubmitForm import SubmitPage

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/login')
driver.maximize_window()

l_page = Login(driver)
l_page.fill_form_emp()
l_page.find_submit()
time.sleep(2)

# i_page = Index(driver)
# i_page.Submit_Quest()
# time.sleep(2)
#
# s_page = SubmitPage(driver)
# s_page.input_request()
# time.sleep(2)
#
# i_page.emp_req()
# r_page = RequestPage(driver)
# r_page.show_all()
# time.sleep(4)
#
# i_page.LogOut()
# time.sleep(4)
#
# l_page.fill_form()
# l_page.find_submit()
# time.sleep(2)
#
# i_page.emp_req()
# r_page.show_all()
# r_page.approve_rem()
# time.sleep(2)
#
# i_page.Stats()
# time.sleep(4)
#
# driver.close()
