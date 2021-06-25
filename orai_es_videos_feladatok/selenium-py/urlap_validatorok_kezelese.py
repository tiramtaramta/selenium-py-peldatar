# validátorok ellenőrzése a beviteli mezők esetében
# azt ellenőrizzük le, hogy megjelenik-e az üzenet és pontosan ugyanez az üzenet jelent-e meg
# required aria-required tag van a html kódban

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/another_form.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    browser.find_element_by_id("submit").click()  # rákattintunk a küldés gombra, hogy megnézzük felugrik-e az üzenet

    validation_message = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='fullname' and @name='fullname']"))).get_attribute("validationMessage")
    # a webdriveren várunk max 20 mp-et addig, amíg az elem meg nem jelenik, amelynek az attributuma a validationmessage

    assert validation_message is not None  # megvizsgáljuk, hogy létezik-e
    assert validation_message == 'Kérjük, töltse ki ezt a mezőt.'

    time.sleep(2)

finally:
    # pass
    browser.close()