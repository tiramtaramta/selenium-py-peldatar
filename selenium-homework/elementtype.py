"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt.
Használj id lokátort és keressd ki az elemenekt egyesével. A legelső olyan elemre ami button típusú kattints rá
és ellenőrizd, hogy a helyes szöveg jelenik-e meg az elemek listája alatt.
A megoldást egy elementtype.py nevű fileban kell beadnod.
"""
from selenium import webdriver

# PATH = "C:\\Windows\\chromedriver.exe" # Másik megoldás, ami elegánsabb
# browser = webdriver.Chrome(PATH)

driver = webdriver.Chrome()


try:
    driver.get("http://localhost:9999/trickyelements.html")

    elements = driver.find_elements_by_xpath('//*[@id]')
    # print(type(elements))

    for element in elements:
        # print(element.tag_name)
        if element == driver.find_element_by_tag_name("button"):
            element.click()
            # print(element.tag_name)
            result = driver.find_element_by_id("result")
            print(result.text)
            break

finally:
    driver.close()

# # solution 2
# try:
#     driver.get("http://localhost:9999/trickyelements.html")
#
#     element1 = driver.find_element_by_id("element1")
#     element2 = driver.find_element_by_id("element2")
#     element3 = driver.find_element_by_id("element3")
#     element4 = driver.find_element_by_id("element4")
#     element5 = driver.find_element_by_id("element5")
#
#     res = driver.find_element_by_id("result")
#
#     tag_list = [element1, element2, element3, element4, element5]
#     for elem in tag_list:
#         if elem.tag_name == "button":
#             elem.click()
#             if res.text == f"{elem.text} vas clicked":
#                 print(f"{elem.text} was clicked and text was right")
#             break
# finally:
#     driver.quit()