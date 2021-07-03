from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://happy-sea-0a5ffef03.azurestaticapps.net/elso.html"

browser = webdriver.Chrome(PATH)


def datas(h, w):
    height_input.send_keys(h)
    weight_input.send_keys(w)
    submit_btn.click()
    time.sleep(3)  # 3 mp várakozás, mielőtt töröljük a beírt értékeket
    height_input.clear()
    weight_input.clear()


try:
    browser.get(URL)

    browser.maximize_window()

    height_input = browser.find_element_by_id("height")
    weight_input = browser.find_element_by_id("weight")
    submit_btn = browser.find_element_by_css_selector("body > input[type=submit]")  # or xpath "//input[@value='computeBMI']"
    your_bmi = browser.find_element_by_id("output")
    this_means = browser.find_element_by_id("comment")

    datas(171, 45)
    assert your_bmi.text == "15"
    assert this_means.text == "Underweight"

    datas(185, 65)
    assert your_bmi.text == "19"
    assert this_means.text == "Normal"

except:
    print("Valami elromlott")

finally:
    browser.quit()
