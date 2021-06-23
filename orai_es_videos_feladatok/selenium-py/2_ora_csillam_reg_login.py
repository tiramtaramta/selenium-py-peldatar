from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://webshop.progmasters.hu/"

"""
CSS alapján keresés a console-ban ==> $$('button')    $$('button[type="submit"]')
Xpath alapján keresés a console-ban ==> $x('//button[@type="submit"]')
"""

browser = webdriver.Chrome(PATH)

browser.maximize_window()
browser.get(URL)

login_btn = browser.find_element_by_id("login")  # megkeressük a login gombot
login_btn.click()
time.sleep(2)

email_input = browser.find_element_by_id("email")  # login oldalon megkeressük az elementeket
password_input = browser.find_element_by_id("password")
# submit_btn = browser.find_element_by_css_selector('button[type="submit"]')
submit_btn = browser.find_element_by_xpath('//button[@type="submit"]')

email_input.send_keys("admin1@gmail.com")
password_input.send_keys("admin1")
submit_btn.click()
time.sleep(2)
browser.quit()

