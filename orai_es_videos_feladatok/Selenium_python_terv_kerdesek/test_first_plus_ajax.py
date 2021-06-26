from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# a pytest csak akkor ismeri fel a teszt osztályokat, ha az osztály nevében szerepel a test szó
# teszt osztályokba több testcase is létrehozható

# a setup és a teardown minden testcase előtt és után meghívódnak.
# Minden testcase külön ablakban fut majd le, egymás után


class TestMySelenium(object):  # nem szabad konstruktort adni neki, csak setup metódust
    def setup(self):  # a self referencián keresztül egy objektumpéldányt létrehozhatunk
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:9999/randomajax.html")

    def teardown(self):  # ha a teszt végzett, ledöntjük, leromboljuk
        self.driver.close()

    def test_first_testcase(self):  # minden driver elé be kell írni a self. részt, mert az osztályhoz tartozik
        self.driver.get("http://localhost:9999/randomajax.html")
        # max 10 mp-et várunk. Az EC könyvtár tartalmaz egyéb feltételeket (megjelenik az elem, aminek az id-ja yes
        yes_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'yes')))
        yes_element.click()
        self.driver.find_element_by_id("buttoncheck").click()
        p = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/p")))
        print(p.text)

    def test_second_testcase(self):  # a kettő hívás közt (setup, teardown) teszt függvények fognak végrehajtódni
        assert True

# majd meghívjuk a terminálban a pytestet a pytest paranccsal