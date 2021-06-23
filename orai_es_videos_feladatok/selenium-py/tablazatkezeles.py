from selenium import webdriver
import csv


def find_and_clear_by_id(id):
    element = browser.find_element_by_id(id)
    element.clear()
    return element


PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/filltablewithsum.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    add_button = browser.find_element_by_id('add')

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            print(row)
            product = find_and_clear_by_id("product").send_keys(row[0])
            quantity = find_and_clear_by_id("quantity").send_keys(row[1])
            price = find_and_clear_by_id("price").send_keys(row[2])
            add_button.click()

    totals = browser.find_element_by_xpath("//table[@id='resultTotals']/tbody/tr/td[3]")  # egyetlen elem kiolvasása
    print(totals.text)

    results_row = browser.find_elements_by_xpath("//table[@id='results']/tbody/tr")  # teljes tábla tartalmának kinyerése
    for row in results_row:
        cells = row.find_elements_by_tag_name("td")
        print(cells[0].text, cells[1].text, cells[2].text)

finally:
    browser.quit()
