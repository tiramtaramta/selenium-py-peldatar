from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/contextmenu.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    ActionChains(browser).context_click().perform()  # ezzel megnyitjuk a context menut

    browser.find_element_by_xpath("//div[@data-rc-launch='first']").click()  # rákattintunk az elemre
    time.sleep(1)
    alert = browser.switch_to.alert  # átlépünk az alertbe
    assert (alert.text == "first")  # összehasonlítjuk a két szöveget
    time.sleep(2)
    alert.accept()  # ezzel eltakarítunk magunk után (elfogadjuk)

finally:
    pass
    # browser.quit()