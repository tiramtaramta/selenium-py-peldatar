# ha van egy form, amiben van egy gomb, ott el tudjuk küldeni az útvonalat
# de a drag and drop módszer már nehézkes  éscsak javascriptes megoldást találunk rá

from selenium import webdriver
from os import getcwd
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/dragndrop3.html"



def drag_and_drop_file(drop_target, path):
    browser = drop_target.parent
    file_input = browser.execute_script(JS_DRAG_DROP, drop_target, 0, 0)  # execute scriptet meghívjuk
    file_input.send_keys(path)

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    file_drag = browser.find_element_by_id("filedrag")
    cwd = getcwd()
    JS_DRAG_DROP = open(cwd + '\\filedrag.js', 'r').read()  # a cél javascriptet felolvassuk
    print(JS_DRAG_DROP)
    time.sleep(2)
    drag_and_drop_file(file_drag, path="C:\\Users\\Gergely\\PycharmProjects\\data.csv")  # nem létezik nálam ilyen!
    time.sleep(5)

finally:
    pass
    # browser.quit()