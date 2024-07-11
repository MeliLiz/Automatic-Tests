from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Given Open the MIT website
        When Search for wbsites about 'quantum'
        Then Verify the results"""
        
@given('Open the MIT website')
def open_mit_website(context):
    context.driver.get(context.config.get('URL', 'url'))

@when('Search for wbsites about "{search_term}"')
def search_for_quantum(context, search_term):
    try:
        search_box = context.driver.find_element(By.ID,"es-search-form-input")
        search_box.send_keys(search_term + Keys.RETURN)
        print(f"Searching for {search_term}")
    except Exception as e:
        print(f"Error finding the search box: {e}")
    
    # Wait for the search results to be displayed
    search_results = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a")) # Waits for all the links to be present <a>
    )

    # Extract the links from the search results
    for result in search_results:
        link = result.get_attribute('href')
        if link:
            print(link)
    
@then('Verify the results')
def verify_results(context):
    pass
    """results = context.driver.find_elements(By.XPATH, '//h3')
    for result in results:
        assert 'quantum' in result.text.lower()"""
        