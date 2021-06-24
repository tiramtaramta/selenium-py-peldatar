# open window javascript eseménnyel van megírva
# new tab pedig egy egyszerű target="_blank"

from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

try:
    browser.get("http://localhost:9999/kitchensink.html")

    # megkeressük a gombot és azonnal rá is kattintunk
    browser.find_element_by_id("openwindow").click()
    time.sleep(1)  # hogy biztosan betöltődjön az új ablak

    # .window_handles 0. eleme, amin éppen most állok (bekerül egy változóba)
    main_window = browser.window_handles[0]

    # .switch_to.window paranccsal átlépek a másik ablakba ( + bekerül egy változóba)
    other_window = browser.switch_to.window('myWin')  # kikereshető, hogy a javascript hogyan nevezi el az új ablakot "myWin"

    # megvizsgáljuk, hogy az oldal title tag-je stimmel-e
    assert(browser.title == "met.hu - Országos Meteorológiai Szolgálat")
    print(browser.title)
    time.sleep(5)
    browser.close()  # bezárjuk az új ablakot
    browser.switch_to.window(main_window) # visszalépünk az eredeti ablakra
    browser.close()  # majd bezárjuk azt is

finally:
    pass  # no operation
    # browser.close()  # csak az éppen aktív ablakot csukja be
    # browser.quit()  # az összes ablakot bezárja