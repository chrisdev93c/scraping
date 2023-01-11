
# Importa los módulos necesarios
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

# Inicializa el webdriver de Brave
driver = webdriver.Chrome(executable_path="C:\\Users\\chris\\Downloads\\chromedriver_win32\\chromedrive.exe")
driver.get("https://www.redpiso.es/alquiler-viviendas/madrid/mostoles")
time.sleep(5)
button = driver.find_element(By.ID, "gdpr-cookie-accept")
button.click()
time.sleep(5)
h3_elements = driver.find_elements(By.TAG_NAME, "h3")
h3_list = []
for h3 in h3_elements:
    h3_list.append(h3.text)
print(h3_list)
time.sleep(5)

driver.close()
