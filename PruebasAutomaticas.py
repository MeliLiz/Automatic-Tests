from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the application home page
driver.get('https://www.google.com')

# Find the search box
search_box = driver.find_element(By.CSS_SELECTOR, '[title="Buscar"]')
search_box.send_keys('Python')
search_box.submit()


# Find the results
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for i, result in enumerate(results):
    print(f'{i + 1}. {result.text}')
    
# Close the browser
driver.quit()
