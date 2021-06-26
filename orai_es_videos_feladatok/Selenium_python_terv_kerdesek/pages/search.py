# itt készül az osztály a test_ddgo.py file-hoz
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    URL = "https://duckduckgo.com"  # url, amin a keresőoldal megtalálható

    SEARCH_INPUT = (By.ID, "search_from_input_homepage")  # lokátortípus és azonosító páros, amin a kereső beviteli mező megtalálható

    def __init__(self, browser):  # inicializálás (kívülről megkapjuk a webdrivert
        self.browser = browser

    def load(self):  # nyissuk meg vele az adott url-t
        self.browser.get(self.URL)

    def search(self, phrase): # írjuk be a kereső kifejezést és kattintsunk az enterre
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)