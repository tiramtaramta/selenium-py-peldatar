"""
Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről. 
Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt. A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás. 
Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet. 
Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát.
"""
import selenium.common.exceptions
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
url_name = input("Kérlek adj meg egy pontos URL-címet: ")
id_name = input("Kérlek adj meg egy ID-nevet: ")

browser = webdriver.Chrome(PATH)

try:
    browser.get(url_name)

    browser.find_element_by_id(id_name)

except selenium.common.exceptions.NoSuchElementException:
    print(f"Nem létezik '{id_name}' nevű elem az oldalon")

finally:
    browser.close()


########### extra megoldás metódussal


# def check_element_by_id(id_name):
#     try:
#         browser.get(url_name)
#
#         browser.find_element_by_id(id_name)
#
#     except selenium.common.exceptions.NoSuchElementException:
#         print(f"Nem létezik {id_name} nevű elem az oldalon")
#
# try:
#     PATH = "C:\\Windows\\chromedriver.exe"  # lehet a try-ban, mert ez is dobhat hibát
#     URL = "http://www.python.org"
#     browser = webdriver.Chrome(PATH)
#     browser.get(URL)
#
#     check_element_by_id("nemletezik")
#
# except:
#     print("Valami más error van")
#
# finally:
#     browser.quit()



