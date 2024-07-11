from selenium import webdriver
from configparser import ConfigParser
from unittest import TestCase

# This will run before all scenarios
def before_all(context):
    context.test = TestCase()
    
    config = ConfigParser()
    config.read('setup.cfg')
    context.config = config # Save the config object to the context
    # print(context.config.get('Browser', 'navegador'))
    """config = ConfigParser()
    config.read('config.ini')
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(10)
    context.browser.get(config['DEFAULT']['url'])"""
  
# This will run after all scenarios  
def after_all(context):
    context.browser.quit()