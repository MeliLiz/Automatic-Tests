from selenium import webdriver
from configparser import ConfigParser
from unittest import TestCase

# This will run before all scenarios
def before_all(context):
    context.test = TestCase()
    
    config = ConfigParser()
    config.read('setup.cfg')
    context.config = config # Save the config object to the context

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://pokemondb.net/pokedex/stats/gen1")
    context.driver = driver # Save the driver object to the context
    
    """table = driver.find_element(By.CLASS_NAME, 'data-table') # Find the table
    body = table.find_element(By.TAG_NAME, 'tbody') # Find the body
    rows = body.find_elements(By.TAG_NAME, 'tr') # Find the rows
    for row in rows:
        print(row.text)"""
  
# This will run after all scenarios  
def after_all(context):
    context.driver.quit()