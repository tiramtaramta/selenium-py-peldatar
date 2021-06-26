from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# nem fontos oop szerint osztályokba rendezni a testcase-eket
# kiszervezhetjük egy újabb függvénybe az ismétlődő elemeket


# decorator pattern. annotációt helyezünk rá.
# fixture-t hozunk létre a függvény előtt, így nem kell beírnunk a többi függvénybe
@pytest.fixture(scope="session")  # a scope-nak köszönhetően az egész futás ugyanazt a böngészőablakot használjuk a session alatt
def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:9999/randomajax.html")
    return driver


def test_first_testcase(browser):  # a teszt függvény bemenő paraméterként megkapja a browser függvényt
    yes_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'yes')))
    yes_element.click()
    browser.find_element_by_id("buttoncheck").click()
    p = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/p")))
    print(p.text)


def test_second_testcase(browser):  # a kettő hívás közt (setup, teardown) teszt függvények fognak végrehajtódni
    assert True

# majd meghívjuk a terminálban a pytestet a pytest paranccsal