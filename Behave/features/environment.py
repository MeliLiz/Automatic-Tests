from selenium import webdriver
from configparser import ConfigParser
from unittest import TestCase
from helper.getBrowser import get_browser

# This will run before all scenarios
def before_all(context):
    context.test = TestCase()
    
    config = ConfigParser()
    config.read('setup.cfg')
    context.config = config # Save the config object to the context

    context.driver = get_browser(context.config.get('Browser', 'navegador')) # Save the driver object to the context
    context.driver.set_window_size(context.config.get('Browser', 'width'), context.config.get('Browser', 'height')) # Set the window size
    
    context.driver.implicitly_wait(10) # Set the implicit wait time
    
  
# This will run after all scenarios  
def after_all(context):
    context.driver.quit()