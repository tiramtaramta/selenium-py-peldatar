# többféle beágyazás lehetséges: pll: widget formában, akár egész oldalként
# nem sokban tér el az ablakok közti navigációktól, de itt nem window.handle-öket használunk,
# hanem iframe elementeket fogunk megkeresni

# a webdriver csak alá- fölérendeltségi viszonyban tud navigálni ezért nem lehet közvetlenül két iframe közt ugrálni
# mindig először a főablakba kell visszatérni és onnan belépni a más iframe-be

from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/embeds.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    # elmentjük változóban a két iframe ablakot
    general_frame = browser.find_element_by_id("general-frame")
    forms_frame = browser.find_element_by_id("forms-frame")

    # bele navigálunk a general_frame-be
    browser.switch_to.frame(general_frame)
    h4_text = browser.find_element_by_tag_name("h4").text  # megkeressük a h4 szöveget

    # kinavigálunk a parent frame-be
    browser.switch_to.parent_frame()

    # belépünk a forms_frame-be
    browser.switch_to.frame(forms_frame)
    browser.find_element_by_id("example-input-text").send_keys(h4_text)  # megkeressük a beviteli mezőt és beadjuk a h4 textet

finally:
    pass
    # browser.quit()