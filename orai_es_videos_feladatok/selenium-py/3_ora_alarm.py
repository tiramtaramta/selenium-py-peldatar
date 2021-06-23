from selenium import webdriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait


PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://techstepacademy.com/training-ground"

browser = webdriver.Chrome(PATH)
browser.get(URL)

try:
    print("I have arrived")
    WebDriverWait(browser, 10).until(alert_is_present())  # vár 10 mp-et, ha addig bármikor kattintok oké, ha nem...
    print("An alarm appeared")
except:
    print("Something went wrong. You should click on a button.")
finally:
    browser.quit()
