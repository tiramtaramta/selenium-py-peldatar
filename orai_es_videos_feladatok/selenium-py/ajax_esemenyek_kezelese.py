# ajaxos események... be van már töltve az oldal, csak nem jelenik meg
# kérés-válasz a háttérben zajlik


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/randomajax.html"


browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    # max 10 mp-et várunk. Az EC könyvtár tartalmaz egyéb feltételeket (megjelenik az elem, aminek az id-ja yes
    yes_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'yes')))
    yes_element.click()
    browser.find_element_by_id("buttoncheck").click()
    p = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/p")))
    print(p.text)

finally:
    pass
    # browser.quit()