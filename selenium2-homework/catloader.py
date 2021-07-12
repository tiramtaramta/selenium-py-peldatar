"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve
és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
"""

from selenium import webdriver
import time


PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/loadmore.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    load_more = browser.find_element_by_xpath("//div[@class='load-more-button']/button")
    pic_num = 0

    for i in range(4):
        time.sleep(3)
        images = browser.find_elements_by_xpath("//div[@class='image']")
        load_more.click()

    for image in images:
        pic_num += 1
        pic_name = f"{pic_num}_{image.find_element_by_tag_name('p').text[8:]}.jpg"
        url = image.find_element_by_tag_name("img").get_attribute("src")
        with open(f'cats/{pic_name}', 'wb') as file:
            file.write(image.screenshot_as_png)
        print(url)
        print(pic_name)
        # #urllib.request.urlretrieve(url, f"../cats/{pic_name}")
        # urllib.request.urlretrieve(url,'/Users/Gergely/Downloads/cat.jpg')

finally:
    # pass
    browser.quit()


