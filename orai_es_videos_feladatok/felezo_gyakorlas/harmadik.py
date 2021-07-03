from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://happy-sea-0a5ffef03.azurestaticapps.net/harmadik.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    browser.maximize_window()

    banner_message = browser.find_element_by_id("banner-message")
    banner_message_btn = browser.find_element_by_xpath('//*[@id="banner-message"]/button')

    if ("alt" in banner_message.get_attribute("class")) is False:  # ha alapból nem alt a stílusa az elemnek
        print("A megfelelő stílusú elem jelent meg az oldalon")
        banner_message_btn.click()

        if ("alt" in banner_message.get_attribute("class")) is True:  # ha kattintás után alt a stílusa az elemnek
            print("A stílus kattintásra megváltozott")
        else:
            print("A stílus kattintásra nem változott meg")

    else:
        print("Nem a megfelelő stílusú elem jelent meg az oldalon")

except:
    print("Valami elromlott")

finally:
    browser.quit()

# Kocka megoldasa

# try:
#     browser.get(URL)
#     browser.maximize_window()
#
#     banner_message = browser.find_element_by_id("banner-message")
#     banner_message_btn = browser.find_element_by_xpath('//button[text()="Change color"]')
#     time.sleep(2)
#     banner_message_btn.click()
#     assert banner_message.get_attribute("class") == "alt"
#     # if banner_message.get_attribute("class") == "alt":
#     #     print("All good")
#
# except:
#     print("Valami elromlott")
#
# finally:
#     browser.quit()
