from behave import given, when, then
from pages.google_page import GooglePage
from utils.read_properties import get_config

@given('the user is on the Google homepage')
def step_open_google(context):
    context.page = GooglePage(context.driver)
    context.driver.get(get_config("url"))

@when('the user enters the search term')
def step_enter_search(context):
    context.page.enter_search_text(get_config("search_text"))

@when('clicks the search button')
def step_click_search(context):
    context.page.click_search()

@then('search results should be displayed')
def step_verify_results(context):
    assert "Selenium" in context.driver.title
