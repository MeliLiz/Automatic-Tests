from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder

@given(u'Validar la cantidad de pokemon de la primera generación')
def step_impl(context):
    pass

@when(u'Se accede a la página de pokedex')
def step_impl(context):
    context.driver.get(context.config.get('URL', 'link'))

@then(u'Validar que existan 151 pokemon')
def step_impl(context):
    table = context.driver.find_element(By.CLASS_NAME, "data-table") # Find the table
    body = table.find_element(By.TAG_NAME, "tbody") # Find the body
    rows = body.find_elements(By.TAG_NAME, "tr") # Find the rows
    context.test.assertEqual(len(rows), 151)
