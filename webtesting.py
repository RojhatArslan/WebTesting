from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.execute_script("window.open('https://google.com', '_blank');")

driver.switch_to.window(driver.window_handles[1])

search_box = driver.find_element(By.NAME,"q")
search_box.clear()

search_box.send_keys("Selenium Python")
driver.implicitly_wait(10)

search_box.send_keys(Keys.RETURN) # Simulates pressing the return key

print("Results page title:",driver.title)


driver.quit()