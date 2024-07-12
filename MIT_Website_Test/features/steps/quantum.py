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
        print("Error finding the search box: {e}")
    # Wait for the search results to be displayed
    search_results = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a")) # Waits for all the links to be present <a>
    )
    print(f"Found {len(search_results)} search results")
    context.test.assertTrue(len(search_results) > 0)
    # context.test.assertEqual(len(search_results), 69300)
    
    
@then('Verify the results')
def verify_results(context): # Verify if there is a page that includes 'A new way for quantum computing systems to keep their cool'
    # Find all the search results
    search_results = context.driver.find_elements(By.TAG_NAME, "h3")
    result_ = None
    for result in search_results:
        print(result.text)
        if result.text == "A new way for quantum computing systems to keep their cool":
            result_ = result
            result.click()
            break
    context.test.assertIsNotNone(result_)

       
        