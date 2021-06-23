"""
Készíts egy Python alkalmazást ami selenium-ot használ.
Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt.
A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás. Feladatot, hogy kezed le ezt a hibát és írj ki
valami emberileg olvasható üzenetet.
Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli
a nemlétező elem tipusú hibát.
"""

from selenium import webdriver

url_name = input("Kérlek adj meg egy pontos URL-címet: ")
element_name = input("Kérlek adj meg egy ID-nevet: ")

driver = webdriver.Chrome()

try:
    driver.get(url_name)

    nems = driver.find_elements_by_id(element_name)

    if len(nems) > 0:
        print(f"Van {element_name} nevű elem az oldalon.")
    else:
        print(f"Nincs {element_name} nevű elem az oldalon.")

finally:
    driver.close()
