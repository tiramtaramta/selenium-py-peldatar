"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:5500/src/windowgame.html oldalt.
A feladatod, hogy megtalád a random kiválasztott színhez tartozó gombot.
Ha egy gombra rákattintasz az egy új ablakot fog feldobni, egy valamilyen színben tündököl.
Ügyelj arra, hogy ne árassza el a képernődet a sok ablak.
"""
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/windowgame.html"
browser = webdriver.Chrome(PATH)

browser.get(URL)

try:
    main_window = browser.window_handles[0]  #
    target_color = browser.find_element_by_id("target_color")
    check_color = target_color.text
    cells = browser.find_elements_by_css_selector('td')  # listába rakjuk a cellákat

    # majd for ciklussal bejárjuk az összes elemét
    for i in cells:
        new_window = i.find_element_by_css_selector("button")
        new_window.click()
        browser.switch_to.window(browser.window_handles[1])
        color_code = browser.find_element_by_css_selector("h1")
        if color_code.text == check_color:
            print("Megtaláltad")
            browser.close()
            browser.switch_to.window(main_window)
            break
        else:
            browser.close()
            browser.switch_to.window(main_window)
except:
    print("Valami hiba történt")
finally:
    browser.quit()