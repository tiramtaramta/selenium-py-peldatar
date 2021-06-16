"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt.
Használj id lokátort és keressd ki az elemenekt egyesével. A legelső olyan elemre ami button típusú kattints rá
és ellenőrizd, hogy a helyes szöveg jelenik-e meg az elemek listája alatt.
A megoldást egy elementtype.py nevű fileban kell beadnod.
"""
from selenium import webdriver

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
