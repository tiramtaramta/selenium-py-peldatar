# a szimulált és a valós egérmozgás közti különbség itt jól megmutatkozik
# a koordináták nem változnak az elemen a mozgatás hatására

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/dragndrop3.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    draggable_element = browser.find_element_by_id("dragThis")
    ActionChains(browser).drag_and_drop_by_offset(draggable_element,
                                                  draggable_element.location["x"] + 350,
                                                  draggable_element.location ["y"] + 100).perform()

finally:
    pass
    # browser.quit()