"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/general.html oldalt.
A feladatod, hogy végiglátogassd az összes linket ezen az oldalon.
Egy link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre rákattintottál,
a megjelent új oldalnak ellenrőizted, hogy eggyezik az urlje az előzőleg használt a tag href-jével
és sikeresen vissza navigáltál a főoldalra. (A tökéletes megoldás nem tartalmaz sor ismétléseket.
Ezt mondjuk függvények írásával is elő tudod idézni.)
"""
from selenium import webdriver

driver = webdriver.Chrome()


try:
    driver.get("http://localhost:9999/general.html")

    links = driver.find_elements_by_xpath("//a[@href]")
    if len(links) > 0:
        for link in links:
            link.click()
            if driver.current_url == link.get_attribute("href"):
                print(link.get_attribute("href") + " OK")
            else:
                print(link.get_attribute("href") + " NOT OK")
            driver.back()
    else:
        print("Nincsenek linkek az oldalon.")

finally:
    driver.close()
