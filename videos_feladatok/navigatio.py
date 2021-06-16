from selenium import webdriver
import time


def navigate_to_general_page():
    link = driver.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/")
    navigate_to_general_page()
    print(driver.current_url)
    # time.sleep(1.0)  # itt egy pillanatra megáll a selenium és vár, hogy lássuk is
    driver.back()
    print(driver.current_url)
    # time.sleep(1.0)
    navigate_to_general_page()

    anchors = driver.find_elements_by_xpath('//header/small//a')

    for a in anchors:
        a.click()
        # time.sleep(1.0)  # legyen lehetőségünk megnézni szemmel is
        print(driver.current_url)  # kiíratjuk a terminálra az url-eket, mert az anchore ott is írja
    print("*" * 50)  # csak a terminálra, hogy lássuk, hol tartunk
    while driver.current_url != "http://localhost:9999/":
        print(driver.current_url)
        driver.back()  # visszalépeget a listán egészen az elejéig

finally:
    driver.close()
