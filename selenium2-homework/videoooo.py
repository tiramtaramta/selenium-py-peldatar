"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.
"""

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
    html5video.send_keys(Keys.SPACE) # a space gombot megnyomva megáll a videó
    time.sleep(5)

    video1 = browser.find_element_by_id("video1")
    video1_btn = browser.find_element_by_xpath('//button[text()="Play/Pause"]')
    video1_btn.click()
    time.sleep(2)
    video1.screenshot("video_scrnshot2.png")
    time.sleep(1)
    video1_btn.click()

    # video2 = browser.find_element_by_xpath('//div[@class="ytp-cued-thumbnail-overlay-image"]')
    video2 = browser.find_element_by_id("youtubeframe")
    video2.click()
    time.sleep(3)
    video2.screenshot("video_scrnshot3.png")
    time.sleep(2)
    video2.click()


finally:
    browser.quit()