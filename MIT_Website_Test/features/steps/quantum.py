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
    # Find all the links of the pages
    pages = context.driver.find_elements(By.CLASS_NAME, 'gsc-cursor-page')
    i = 0
    while i < len(pages):
        
        # Encuentra todos los resultados de búsqueda en la página actual
        search_results = context.driver.find_elements(By.CLASS_NAME, "gs-title")
        
        # Itera a través de cada resultado en la página actual
        for result in search_results:
            print(result.text)
            if "A new way for quantum computing systems to keep their cool" in result.text:
                result.click()
                result_found = True
                break
        
        if result_found:
            break  # Sal del bucle si se encuentra el resultado
        
        # Verifica si hay una página siguiente y navega a ella
        try:
            # Verifica si el siguiente botón de página existe
            if i+1 < len(pages):
                next_button = pages[i+1]
                print(next_button.text)
                # Desplázate al elemento next_button
                context.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                print("Desplazando")
                # Haz clic en el elemento utilizando JavaScript
                context.driver.execute_script("arguments[0].click();", next_button)
                print("Clicking")
                search_results = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a")) # Waits for all the links to be present <a>
                )
            else:
                raise Exception("No more pages available.")
        except Exception as e:
            print(f"No more pages available or error navigating to next page: {e}")
            break
        
        i += 1
    
    # Asegúrate de que se encontró el resultado
    assert result_found, "The expected search result was not found."
