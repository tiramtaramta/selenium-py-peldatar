"""
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
ID alapján
NAME alapján
XPath kifejezéssel Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.
"""
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    element_by_id = driver.find_element_by_id("mousehover")
    print(f"Element by id: " + element_by_id.text)

    element_by_name = driver.find_element_by_name("courses")
    print(f"Element by name: " + element_by_name.text)

    element_by_xpath = driver.find_element_by_xpath('//*[@id="hondacheck"]')
    print(f"Element by Xpath: " + element_by_xpath.get_attribute("value"))

finally:
    driver.close()

# # solution 2
# # By id
# car_menu = driver.find_element_by_id("carselect")
# my_cars = Select(car_menu)
# for i in my_cars.options:
#     print(i.text)
#
# # By name
# table = driver.find_element_by_name("courses")
# print(table.text)
#
# # by xpath
# element_xpath = driver.find_element_by_xpath("//legend[text()='Switch to Window Example']")
# print(element_xpath.text)
#
# # print attribute value
# elem_by_id = driver.find_element_by_id('hide-textbox').get_attribute("type")
# print(elem_by_id)