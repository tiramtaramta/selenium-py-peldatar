"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/dragndrop2.html oldalt.
A feladatod, hogy a todo oszlobpól átrakd az összes kártyát a doing oszlopba.
Szükség lesz a dnd.js file-ra is
"""

import time
from os import getcwd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/dragndrop2.html"
options = Options()

options.add_argument('--disable-gpu')
browser = webdriver.Chrome(PATH)
browser.maximize_window()

try:
    browser.get(URL)
    time.sleep(3)

    cwd = getcwd()
    JS_DRAG_DROP = open(cwd + '\\dnd.js', 'r').read()
    print(JS_DRAG_DROP)
    # drag and drop elemenként
    source_ids = ("Pizza", "Tacos", "BBQ", "Burgers")
    for id in source_ids:
        source = browser.find_element_by_id(id)
        target = browser.find_element_by_id("Doing")

        browser.execute_script(JS_DRAG_DROP, source, target)

    browser.implicitly_wait(3)

finally:
    # pass
    browser.quit()