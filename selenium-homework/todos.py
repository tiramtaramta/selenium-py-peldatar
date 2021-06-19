"""
A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
A feladatod, hogy kigyűjtsd az összes jelenleg aktív Todo bejegyzést.
Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg.
(Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).
A megoldást egy todos.py nevű fileban kell beadnod.
"""

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/todo.html")

    done_falses = driver.find_elements_by_xpath('//span[@class="done-false"]')

    for done_false in done_falses:
        elements = done_false.text
        print(elements)

finally:
    driver.close()
