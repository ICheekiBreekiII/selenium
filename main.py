from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import login

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://login.nstu.ru/ssoservice/XUI/#login/&goto=http%3A%2F%2Fciu.nstu.ru%2Fstudent_study%2F")

time.sleep(2)
elem = driver.find_element_by_name("callback_0")
elem.clear()
elem.send_keys(login.log)
elem = driver.find_element_by_name("callback_1")
elem.clear()
elem.send_keys(login.passw)
elem = driver.find_element_by_name("callback_2")
elem.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()
