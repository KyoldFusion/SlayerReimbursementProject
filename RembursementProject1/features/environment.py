from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def before_step(context, step):
    pass


def before_Scenario(context, scenario):
    # We might want to get the url here because we have two scenarios which involve logging in

    pass


def before_feature(context, feature):
    pass


def before_tag(context, tag):
    pass


def after_all(context):
    pass


def after_step(context, step):
    pass


def after_scenario(context, step):
    pass


def after_tag(context, step):
    pass


def after_all(context):
    # remember to close the browser
    pass
