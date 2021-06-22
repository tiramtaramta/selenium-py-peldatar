from selenium import webdriver
import csv
import time

driver = webdriver.Chrome()
driver.get('http://localhost:9999/another_form.html')


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


add_button = driver.find_element_by_id("submit")

with open('table_in.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        print(row)
        fullname = find_and_clear_by_id("fullname").send_keys(row[0])
        email = find_and_clear_by_id("email").send_keys(row[1])
        date = find_and_clear_by_id("dob").send_keys(row[2])
        phone = find_and_clear_by_id("phone").send_keys(row[3])
        add_button.click()
    export = driver.find_element_by_xpath('/html/body/main/div/button')
    export.click()

