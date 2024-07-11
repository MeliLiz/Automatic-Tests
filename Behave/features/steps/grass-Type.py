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
    
"""Given Validar la cantidad de pokemon de tipo pasto de la primera generación
        When Se accede a la página de pokedex
        Then Validar que existan 14 pokemon de tipo pasto"""
        
@given(u'Validar la cantidad de pokemon de tipo pasto de la primera generación')
def step_impl(context):
    pass

@then(u'Validar que existan 14 pokemon de tipo pasto')
def step_impl(context):
    table = context.driver.find_element(By.CLASS_NAME, "data-table")
    body = table.find_element(By.TAG_NAME, "tbody")
    grass_type = body.find_elements(By.CLASS_NAME, "type-grass")
    context.test.assertEqual(len(grass_type), 14)
    
"""Given Validar la cantidad de los diferentes tipos de pokemon de la primera generación
        When Se accede a la página de pokedex
        Then Validar que la cantidad de tipo <pokemonType> sea <n>"""
        
@given(u'Validar la cantidad de los diferentes tipos de pokemon de la primera generación')
def step_impl(context):
    pass

@then(u'Validar que la cantidad de tipo {pokemonType} sea {n}')
def step_impl(context, pokemonType, n):
    table = context.driver.find_element(By.CLASS_NAME, "data-table")
    body = table.find_element(By.TAG_NAME, "tbody")
    type = body.find_elements(By.CLASS_NAME, "type-{pokemonType}")
    context.test.assertEqual(len(type), int(n))
