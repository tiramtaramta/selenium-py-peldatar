# html alertek kezelése!!!
"""
az alertek látszólag nem tesztelhetők, mert nem a weblapon jelennek meg, hanem a natív alkalmazásban
Így nincs kiválasztható elem az oldalról a tesztelésére.
Az alert megfogja az oldal működését.
Becsukáskor ott folytatja a weboldal, ahol abbahagytuk a munkát.
"""
from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

try:
    browser.get("http://localhost:9999/kitchensink.html")

    # alert esetén arra utasítjuk a webdrivert, hogy csatlakozzon ahhoz a folyamathoz, ami az alertet felhozta
    # hogy az alertben levő dolgokat ellenőrizhessük

    name = browser.find_element_by_id("name")
    button = browser.find_element_by_id("alertbtn")

    name.send_keys("Gergő")
    button.click()

    ref_text = "Hello Gergő, share this practice page and share your knowledge"  # amit vissza kell kapnunk
    # ablak, alert, tab-ra váltás mindig switch_to paranccsal történik!!!
    alert = browser.switch_to.alert  # elmentjük egy alert változóban
    assert(alert.text == ref_text)  # az assert segítségével összehasonlítjuk
    print(alert.text)

    # hogyan zárjuk be az alertet?
    time.sleep(2)
    alert.accept()  # az accept függvényt meghívjuk rá és az elfogadja (okét nyom)

finally:
    # pass  # no operation
    browser.quit()  # az egész ablakot becsukja