"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt.
A tanultak alapján az összes alert funkcióra írj selenium kódot.
A prompt-nál teszteld le, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.
"""

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

try:
    browser.get("http://localhost:9999/alert_playground.html")
    # alert button
    alert_button = browser.find_element_by_name("alert")
    alert_button.click()

    ref_text = "I am alert"
    alert = browser.switch_to.alert
    assert(alert.text == ref_text)
    print(alert.text)

    time.sleep(2)
    alert.accept()


    # confirmation button
    confirmation_button = browser.find_element_by_name("confirmation")
    confirmation_button.click()

    ref_text = "I am confirm"
    confirmation = browser.switch_to.alert
    assert (confirmation.text == ref_text)
    print(confirmation.text)

    time.sleep(2)
    alert.accept()


    # prompt button
    prompt_button = browser.find_element_by_name("prompt")
    prompt_button.click()

    prompt = browser.switch_to.alert
    test_text = prompt.send_keys("I am prompt")

    time.sleep(2)
    alert.accept()

    demo = browser.find_element_by_xpath("//*[@id='demo']")
    print(demo.text)


    # double click me
    action = ActionChains(browser)
    double_button = browser.find_element_by_id("double-click")
    action.double_click(on_element=double_button).perform()

    ref_text = "You double clicked me!!!, You got to be kidding me"
    alert = browser.switch_to.alert
    assert (alert.text == ref_text)
    print(alert.text)

    time.sleep(2)
    alert.accept()

finally:
    # pass  # no operation
    browser.quit()  # az egész ablakot becsukja