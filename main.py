from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://www.google.com")

time.sleep(2)
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()