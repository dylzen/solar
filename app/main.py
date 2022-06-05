from tracemalloc import start
import config
import ops
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = ops.start_driver()
driver.get(config.login_url)
print(driver.title)
print("Logging in...")
username_textbox=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME,"username")))
username_textbox.send_keys(config.username)
password_textbox=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.NAME,"password")))
password_textbox.send_keys(config.password)
login_button=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID,"login-btn")))
login_button.click()
print("Fetching data...")
battery_percentage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'TSoc_value')))
battery_percentage_text = battery_percentage.text
battery_percentage_float = float(battery_percentage.text)
photovoltaic_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'photovoltaic-measure')))
battery_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'battery-measure')))
grid_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'grid-measure')))
global_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'GlobState_value')))
inverter_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'InvState_value')))
date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="c-card-header-timestamp"] cux-card-timestamp')))
print("Creating strings...")
battery_percentage_string = "Percentuale batterie: "+battery_percentage.text+"%"
print(battery_percentage_string)
photovoltaic_measure_string = "Energia da fotovoltaico: "+photovoltaic_measure.text
battery_measure_string = "Consumo da batterie: "+battery_measure.text
grid_measure_string = "Erogazione alla rete: "+grid_measure.text
global_state_string = "Stato globale: "+global_state.text
inverter_state_string = "Stato inverter: "+inverter_state.text
date_string = "Data/ora: "+date.text

ops.send_msg(battery_percentage_string+"\n"+photovoltaic_measure_string+"\n"+battery_measure_string+"\n"+grid_measure_string+"\n"+global_state_string+"\n"+inverter_state_string+"\n"+date_string)

print("Done.")