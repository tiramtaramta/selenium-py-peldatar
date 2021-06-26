from selenium import webdriver
import time

# a pytest csak akkor ismeri fel a teszt osztályokat, ha az osztály nevében szerepel a test szó
# teszt osztályokba több testcase is létrehozható

# a setup és a teardown minden testcase előtt és után meghívódnak.
# Minden testcase külön ablakban fut majd le, egymás után


class TestMySelenium(object):  # nem szabad konstruktort adni neki, csak setup metódust
    def setup(self):  # a self referencián keresztül egy objektumpéldányt létrehozhatunk
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:999")

    def teardown(self):  # ha a teszt végzett, ledöntjük, leromboljuk
        self.driver.close()

    def test_first_testcase(self):  # a kettő hívás közt (setup, teardown) teszt függvények fognak végrehajtódni
        time.sleep(2)
        assert False

    def test_second_testcase(self):  # a kettő hívás közt (setup, teardown) teszt függvények fognak végrehajtódni
        assert True

# majd meghívjuk a terminálban a pytestet a pytest paranccsal