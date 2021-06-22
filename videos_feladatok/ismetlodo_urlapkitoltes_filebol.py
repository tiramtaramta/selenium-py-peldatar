import csv
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/filltablewithsum.html")


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


add_button = driver.find_element_by_id('add')


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # fejléc átugrása
    for row in csv_reader:
        print(row)
        product = find_and_clear_by_id("product").send_keys(row[0])
        # az alábbi sorokat váltottuk ki függvénnyel és fűztük össze a harmadik lépéssel
        # product = driver.find_element_by_id("product")
        # product.clear()  # belekattint és kitöröl
        # product.send_keys(row[0]) # beírja a sor nulladik elemét

        quantity = find_and_clear_by_id("quantity").send_keys(row[1])
        # az alábbi sorokat váltottuk ki függvénnyel és fűztük össze a harmadik lépéssel
        # quantity = driver.find_element_by_id("quantity")
        # quantity.clear()  # belekattint és kitöröl
        # quantity.send_keys(row[1])  # beírja a sor első elemét

        price = find_and_clear_by_id("price").send_keys(row[2])
        # az alábbi sorokat váltottuk ki függvénnyel és fűztük össze a harmadik lépéssel
        # price = driver.find_element_by_id("price")
        # price.clear()  # belekattint és kitöröl
        # price.send_keys(row[2])  # beírja a sor második elemét

        add_button.click()
        # driver.find_element_by_id('add').click()  # az add gombot megnyomjuk
