import pytest
from selenium.webdriver import Chrome
import time
from pages.search import DuckDuckGoSearchPage  # beimportáljuk a search file-ból az adott függvényt (metódust)
from pages.results import DuckDuckGoResultPage  # importáljuk a results fileból az adott függvényt

@pytest.fixture
def browser():
    # inicializáljuk a chromedrivert
    driver = Chrome()
    # megvárjuk, hogy minden betöltődjön, mielőtt bármit csinálunk
    driver.implicitly_wait(10)

    # visszatérő érték a driver
    return driver


def test_basic_duckduckgo_search(browser):
    PHRASE = "panda"

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()  # töltse be az oldalt

    time.sleep(3)

    search_page.search(PHRASE)  # futtassa le a keresést
    time.sleep(3)
    result_page = DuckDuckGoResultPage(browser)  # a result page-nek átadjuk a browsert




    # majd ellenőrzi a kapott értékeket
    assert result_page.link_div_count() > 0  # a result oldalon található metódus
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE