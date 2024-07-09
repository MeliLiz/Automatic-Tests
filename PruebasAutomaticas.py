from selenium import webdriver
from selenium.webdriver.common.by import By

# Se crea una instancia de Chrome
driver = webdriver.Chrome()

# Se navega a la página de Google
driver.get('https://www.google.com')


search_box = driver.find_element(By.CSS_SELECTOR, '[title="Buscar"]')
search_box.send_keys('Python')
search_box.submit()


# Enumerar los resultados de la búsqueda
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for i, result in enumerate(results):
    print(f'{i + 1}. {result.text}')
    
# Cerrar el navegador
driver.quit()
