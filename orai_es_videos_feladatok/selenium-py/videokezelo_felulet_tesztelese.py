# videólejátszókat szinte csak billentyűzetről lehet tesztelni, ezért kell a common.keys
# valódi bizonyítékot ezzel nem tudunk szerezni, hogy tényleg elindult-e a lejátszás, de részmegoldásnak jó

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/videos.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    html5video = browser.find_element_by_id("html5video")  # megkeressük a videó elemet
    html5video.click()  # ezzel csak kiválasztjuk az elemet
    html5video.send_keys(Keys.SPACE)  # a space gombot megnyomva elindul a videó
    time.sleep(4)
    html5video.screenshot("video_scrnshot.png")  # rövid késleltetés után csinálunk egy screenshot-ot

    time.sleep(5)
finally:
    browser.quit()