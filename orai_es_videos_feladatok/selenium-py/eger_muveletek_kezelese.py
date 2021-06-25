# az egérmutatóról semmit nem tud maga a böngésző... csak a felé ér egy elemnek (hover)
# vagy arról, ha megnyomunk vele valamit
# erre is van egy külön könyvtár seleniumon belül action chance
# seleniumból egyáltalán nem vezérelhető az egér, csak az alacsony szintű egérműveleteket tudjuk szimulálni
# (mintha oda vittük volna)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    mouse_hover = browser.find_element_by_id("mousehover") # megkeressük a hoverre reagáló gombot
    top_submenu = browser.find_element_by_xpath("//div[@class='mouse-hover-content']/a[1]")  # a lenyíló első elemét

    # builder pattern ==> itt csak előkészítjük a műveleteket
    actions = ActionChains(browser)  # változóban elmentjük a webdrivert átadva az actionchains-nek
    actions.move_to_element(mouse_hover)  # mozogjon a mousehover gomb felé
    actions.click(top_submenu)
    # és itt futtatjuk le
    actions.perform()

    # # elegánsabb megoldás
    # mouse_hover = browser.find_element_by_id("mousehover")  # megkeressük a hoverre reagáló gombot
    # top_submenu = browser.find_element_by_xpath("//div[@class='mouse-hover-content']/a[1]")  # a lenyíló első elemét
    # time.sleep(2)
    # ActionChains(browser).move_to_element(mouse_hover).perform()
    # time.sleep(3)
    # # builder pattern ==> itt csak előkészítjük a műveleteket
    # actions = ActionChains(browser)  # változóban elmentjük a webdrivert átadva az actionchains-nek
    # actions.click(top_submenu)
    # # és itt futtatjuk le
    # actions.perform()

finally:
    browser.quit()
    # pass