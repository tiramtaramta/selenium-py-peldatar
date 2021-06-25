# ha szövegként be tudok olvasni javascriptet, amit értelmezni tud a böngésző
# akkor meg tudom kérni a drivert, hogy töltse be és futtassa le
# script injection, melyre ráhívunk

from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    js = "alert('Hello, World!');"  # javascriptben kell a pontosvessző
    browser.execute_script(js)  # futtassa a driver a js változót execute script segítségével

finally:
    browser.close()