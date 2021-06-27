"""
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt.
A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
a) Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
b) Ellenőrizd a kereső funkciót.
c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/editable-table.html"

browser = webdriver.Chrome(PATH)


def row_adds_with_content(row):
    add_button.click()
    time.sleep(2)
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[1]/input").send_keys(row[0])
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[2]/input").send_keys(row[1])
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").clear()
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").send_keys(row[2])
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[4]/input").send_keys(row[3])


def update_row_element(row):
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").clear()
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").send_keys(row[2])


def table_print():
    list = []
    rows = browser.find_elements_by_xpath("//tbody/tr[@class='eachRow']/td/input")
    for row in rows:
        list.append(row.get_attribute('value'))
    print(', '.join(map(str, list)))


try:
    browser.get(URL)
    add_button = browser.find_element_by_xpath('//*[@id="container"]//button')
    first_row = ["tirarira", "190", "4", "Electronics"]
    second_row = ["macska", "120", "3", "Electronincs"]
    update_row = [" ", " ", "40", " "]
    word = "bas"

    # sorok hozzáadása
    row_adds_with_content(first_row)
    row_adds_with_content(second_row)
    # a táblázat ellenőrzése printeléssel
    table_print()

    # a táblázat elemének felülírása
    update_row_element(update_row)
    # a update-elt táblázat ellenőrzése printeléssel
    table_print()

    # keresőmező ellenőrzése
    browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/input').send_keys(word)
    time.sleep(2)
    # a szűkített táblázat ellenőrzése printeléssel
    table_print()
    # keresőmező törlése
    browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/input').clear()

    time.sleep(5)
finally:
    browser.quit()
