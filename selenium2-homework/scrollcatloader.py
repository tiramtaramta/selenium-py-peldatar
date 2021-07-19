"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/scrolltoload.html oldalt.
Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve
és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
(ez a feladat majdnem ugyan az, mint az előző feladat, csakhogy nincs load more gomb.)
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/scrolltoload.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    js = "window.scrollTo(0,2000)"
    browser.execute_script(js)
    pic_num = 0
    images = []

    while True:
        images = browser.find_elements_by_xpath("//div[@class='image']")
        if len(images) >= 20:
            break
        time.sleep(2)

        html = browser.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

    for image in images[0:20]:
        pic_num += 1
        pic_name = f"{pic_num}_{image.find_element_by_tag_name('p').text[8:]}.jpg"
        url = image.find_element_by_tag_name("img").get_attribute("src")
        with open(f'cat/{pic_name}', 'wb') as file:
            file.write(image.screenshot_as_png)
        print(url)
        print(pic_name)

finally:
    browser.quit()