# flex és grid elrendezések
from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/responsive-table.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    browser.set_window_size(800, 1080)  # ezzel átméretezhetjük az ablak méretét
    size = browser.get_window_size()  # lekérdezzük az ablak méretét és elátroljuk
    print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))  # majd kiíratjuk
    time.sleep(2)
    browser.set_window_size(240, 1080)  # majd újra
    size = browser.get_window_size()  # lekérdezzük az ablak méretét és elátroljuk
    print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))  # majd kiíratjuk
    time.sleep(2)

    # a végeredmény el fog térni, mert a beállítások csak javaslatok... a webdriver dönti el, hogy mekkorára áll át

finally:
    pass
    # browser.quit()