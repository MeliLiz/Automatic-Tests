from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

"""
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
"""

"""
# With DuckDuckGo
driver.get('https://start.duckduckgo.com')
search_box = driver.find_element(By.ID, 'searchbox_input')
search_box.send_keys('Python')
search_box.submit()

# Find the results
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for i, result in enumerate(results):
    print(f'{i + 1}. {result.text}')
    
# Select the first result
sel = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div/h2/a[1]')
sel.click()
print(driver.current_url)
"""
# With PokemonDB
driver.get("https://pokemondb.net/pokedex/stats/gen1")
table = driver.find_element(By.CLASS_NAME, 'data-table') # Find the table
body = table.find_element(By.TAG_NAME, 'tbody') # Find the body
rows = body.find_elements(By.TAG_NAME, 'tr') # Find the rows
for row in rows:
    print(row.text)
    """cells = row.find_elements(By.TAG_NAME, 'td') # Find the cells
    for i, cell in enumerate(cells):
        if i == 1:
            print(cell.text)
            break"""


