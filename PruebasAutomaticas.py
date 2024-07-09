from selenium import webdriver
from selenium.webdriver.common.by import By

# Se crea una instancia de Chrome
driver = webdriver.Chrome()

# Se navega a la página de Google
driver.get('https://www.google.com')


search_box = driver.find_element(By.CSS_SELECTOR, '[title="Buscar"]')
search_box.send_keys('Python')
search_box.submit()
"""text_box = driver.find_element(By.NAME, 'q')
text_box.send_keys('Python')
text_box.submit()"""
