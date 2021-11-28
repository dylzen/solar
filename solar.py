import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(config.login_url)
print(driver.title)

username_textbox=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME,"username")))
username_textbox.send_keys(config.username)
password_textbox=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.NAME,"password")))
password_textbox.send_keys(config.password)
login_button=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID,"login-btn")))
login_button.click()


battery_percentage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'TSoc_value')))
print("Percentuale batterie: "+battery_percentage.text+"%")
photovoltaic_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'photovoltaic-measure')))
print("Fotovoltaico: "+photovoltaic_measure.text)
battery_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'battery-measure')))
print("Batterie: "+battery_measure.text)
grid_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'grid-measure')))
print("Rete: "+grid_measure.text)
date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="c-card-header-timestamp"] cux-card-timestamp')))
print("Data/ora: "+date.text)

driver.stop_client()
driver.close()
driver.quit()
