from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder

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

"""
# With PokemonDB
driver.get("https://pokemondb.net/pokedex/stats/gen1")
table = driver.find_element(By.CLASS_NAME, 'data-table') # Find the table
body = table.find_element(By.TAG_NAME, 'tbody') # Find the body
rows = body.find_elements(By.TAG_NAME, 'tr') # Find the rows
for row in rows:
    print(row.text)
    
"""


driver.get("https://pokemondb.net/pokedex/stats/gen1")
table = driver.find_element(By.CLASS_NAME, 'data-table') # Find the table
body = table.find_element(By.TAG_NAME, 'tbody') # Find the body
grass_type = body.find_elements(By.Class_NAME, 'type-grass') # Find the rows
print(len(grass_type))
# Search the type grass and get the results
#type_filter = driver.find_element(By.XPATH, '//*[@id="filter-pkmn-type"]')
# Select the type grass
#type_filter.click()
#driver.find_element(By.XPATH, '//option[text()="Grass"]').click()


"""
# Get the classes of Facultad de Ciencias
driver.get("https://www.fciencias.unam.mx/")
head = driver.find_element(By.XPATH, '/html/body/div/div/header/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/nav/div/div/ul/li[1]/a')
hover = ActionChains(driver).move_to_element(head)
hover.perform()

cc = driver.find_element(By.XPATH, '/html/body/div/div/header/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/nav/div/div/ul/li[1]/a')
cc.click()

ActionBuilder(driver).clear_actions()

"""


