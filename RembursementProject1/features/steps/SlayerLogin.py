from behave import *
from selenium.webdriver.common.keys import Keys
import time


@given('a user is on the login page of Slayer Reimbursements')
def test_log_home(context):
    context.driver.get('http://127.0.0.1:5000/login')
    time.sleep(2)


@when('a user enters the correct Username and password')
def test_user_enters_creds(context):
    context.driver.find_element_by_name("username").send_keys("heal")
    context.driver.find_element_by_name("password").send_keys("everybody")
    context.driver.find_element_by_id("login").click()
    time.sleep(2)

@then('The user will be brought to the index page')
def test_bring_index(context):
    assert 'index' in context.driver.current_url


@given('A user is on the home page of Slayer Reimbursements')
def test_home_submit(context):
    assert 'index' in context.driver.current_url


@when('the user clicks the "Submit Request" Button, the user will be brought to the Submit Request Page')
def move_to_submit(context):
    context.driver.find_element_by_link_text('Submit Request').click()
    time.sleep(3)


@then('the user is redirected to submit a request on the newly developed form')
def reimbursement_page(context):
    assert 'submit' in context.driver.current_url


@given('A user has accessed the Reimbursement page')
def submit_page(context):
    assert 'submit' in context.driver.current_url
    time.sleep(1)


@when(
    'The user enters the price/economy of their reimbursement stating why they are submitting their reimbursement with their manager')
def fill_forms(context):
    context.driver.find_element_by_id('economy').send_keys("1000")
    context.driver.find_element_by_id('purpose').send_keys("automation test")


@then('they will be able to submit their request to a manager')
def change_to_pending(context):
    context.driver.find_element_by_link_text('Requests').click()
    time.sleep(2)
    assert 'pending' in context.driver.current_url


@given('A user has submitted their reimbursement and has clicked the "Request" Tab')
def pending_verified(context):
    assert 'pending' in context.driver.current_url


@when('the user clicks the request tab they are brought to the request page where they can see their history')
def pending_tab(context):
    assert 'pending' in context.driver.current_url


@Then(
    'the user chooses "pending" to check to see if their request has made it in the system successfully been submitted')
def verify_submission(context):
    context.driver.find_element_by_id('pending').click()
    time.sleep(2)


@given('The user has submitted their Reimbursement and would like to log out at the end of the day')
def verify_submission(context):
    assert 'pending' in context.driver.current_url


@when('The user clicks the notification symbol in the top right corner they will see a prompt for logout')
def notif_click(context):
    context.driver.find_element_by_id("navbarDropdownMenuLink").click()
    time.sleep(1)


@then('the user will click then button to log out of their account and the user will successfully be logged out.')
def log_out(context):
    context.driver.find_element_by_id("logout").click()
    time.sleep(2)


@given('a manager is on the login page of Slayer Reimbursements')
def test_log_home_manager(context):
    assert 'login' in context.driver.current_url


@when('a manager enters the correct Username and password')
def test_manager_enters_creds(context):
    context.driver.find_element_by_name("username").send_keys("hotboy")
    context.driver.find_element_by_name("password").send_keys("gutted")
    context.driver.find_element_by_id("login").click()
    time.sleep(2)


@then('the manager is brought to the index page for managers')
def test_manager_home(context):
    assert 'index' in context.driver.current_url
    time.sleep(2)


@given('The manager is on the home page and logged in')
def test_move_manager_request(context):
    assert 'index' in context.driver.current_url


@when('The manager clicks the requests tab they will be brought to their pending page')
def select_requests_page(context):
    context.driver.find_element_by_link_text('Requests').click()
    time.sleep(2)


@then('the manager will be able to approve their pending reimbursements and the table will auto update')
def update_pending_status(context):
    R_ID = "reimburse"
    Purpose = "purpose"
    approve = "approved_reim"
    context.driver.find_element_by_id('pending').click()
    time.sleep(2)
    context.driver.find_element_by_id(R_ID).send_keys("26")
    context.driver.find_element_by_id(Purpose).send_keys('Auto Approval')
    context.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(2)
    context.driver.find_element_by_id(approve).click()
    time.sleep(4)
    context.driver.find_element_by_id('approved').click()
    time.sleep(7)


@given('The manager has recently approved a request and would like to check statistics')
def check_stats_pre(context):
    assert 'pending' in context.driver.current_url


@when('the manager clicks the statistics tab they will be brought to the statistics page')
def go_to_stats(context):
    context.driver.find_element_by_link_text('Statistics').click()
    time.sleep(2)


@then('the manager can scrolldown to see different variations of measurement and graphs')
def scroll_Stats(context):
    context.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    context.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(4)
    context.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(4)
    assert 'statistics' in context.driver.current_url
