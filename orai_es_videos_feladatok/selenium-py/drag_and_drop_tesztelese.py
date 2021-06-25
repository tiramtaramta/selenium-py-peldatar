# 2016 óta nincs támogatás
# html4-nél működik, html5 esetében egyáltalán nem lehetséges javascript nélkül
# elkerülő megoldás van csak rá

from selenium import webdriver
import time
from os import getcwd

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/dragndrop1.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    time.sleep(2)

    cwd = getcwd()
    JS_DRAG_DROP = open(cwd + '\\drag-drop.js', 'r').read()
    print(JS_DRAG_DROP)
    # drag and drop an element on another one
    source = browser.find_element_by_id("drag1")
    target = browser.find_element_by_id("div2")

    browser.execute_script(JS_DRAG_DROP, source, target)

    browser.implicitly_wait(5)


finally:
    browser.quit()