from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # ez működteti a billentyűzet egyéb gombjait
import time

####### SEND KEYS
PATH = "C:\\Windows\\chromedriver.exe"
URL = 'http://localhost:9999/simplevalidation.html'

browser = webdriver.Chrome(PATH)
browser.get(URL)

email_field = browser.find_element_by_id("test-email")
password_field = browser.find_element_by_id("test-password")
confirm_password = browser.find_element_by_id("test-confirm-password")

email_field.send_keys("valami@gmail.com")
email_field.send_keys(Keys.TAB)
time.sleep(3)
password_field.send_keys("egycicamegegykuutya")
password_field.send_keys(Keys.TAB)
time.sleep(3)
confirm_password.send_keys("egycicamegegykuutya")
confirm_password(Keys.TAB)
time.sleep(3)
