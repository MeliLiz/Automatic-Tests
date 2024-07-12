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
    
    
@then('Verify the results')
def verify_results(context):
    result_found = False
    # Find the number of pages in the search results
    len_pages = len(context.driver.find_elements(By.CLASS_NAME, 'gsc-cursor-page'))
    i = 0
    while i < len_pages:
        print("i: ", i)
        # Find all the search results on the current page
        search_results = context.driver.find_elements(By.CLASS_NAME, "gs-title")
        
        # Iterate through the search results
        for result in search_results:
            print(result.text)
            if "A new way for quantum computing systems to keep their cool" in result.text:
                result.click()
                result_found = True
                break
        
        if result_found:
            print("Result found")
            break  # Exit the loop if the result is found, no need to check other pages
        
        # Verify if there are more pages available
        try:
            # Find all the page buttons
            pages = context.driver.find_elements(By.CLASS_NAME, 'gsc-cursor-page')
            # Verify if there is a next button
            if i+1 < len(pages):
                next_button = pages[i+1]  # Get the next button
                print(next_button.text)
                # Scroll to the next button
                context.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                print("Desplazando")
                # Click the next button
                context.driver.execute_script("arguments[0].click();", next_button)
                print("Clicking")
                # Wait for the old search results to disappear
                WebDriverWait(context.driver, 10).until(
                    EC.staleness_of(search_results[0])
                )
                # Wait for the new search results to be displayed
                WebDriverWait(context.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "gs-title"))
                )
            else:
                raise Exception("No more pages available.")
        except Exception as e:
            print(f"No more pages available or error navigating to next page: {e}")
            break
        
        i += 1
    
    # Asegúrate de que se encontró el resultado
    context.test.assertTrue(result_found)
