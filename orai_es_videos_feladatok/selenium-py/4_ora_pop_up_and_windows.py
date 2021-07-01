###  POP UPS  ####################

import time
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    alert_button = browser.find_element_by_id('alertbtn')
    alert_button.click()

    alert_pop = browser.switch_to.alert  # átváltunk switch-csel a felugró ablakba
    assert(alert_pop.text == "Hello , share this practice page and share your knowledge")
    # if alert_pop.text == "Hello , Are you sure you want to confirm?":
    #     print("All good")  # az assertes megoldás szebb

    # assertel megvizsgáljuk, hogy a felugró ablak text-je megegyezik-e azzal, amit szeretnénk
    time.sleep(2)
    alert_pop.accept()  # a felugró ablaknak nincs elérhetősége a DOM-ban, ezért accept/dismiss

except:
    print("Valami hiba történt")

finally:
    browser.quit()


###  NEW Window  ###################

try:
    browser.get(URL)

    open_new_tab_btn = browser.find_element_by_id('opentab')
    open_new_tab_btn.click()  # megnyitjuk az új ablakot

    # TABokat kezeld kb ugy mintha egy lista lenne az
    main_window = browser.window_handles[0]  # a main-nek elnevezem a fő ablakot
    browser.switch_to.window(browser.window_handles[1])  # átnavigálok a második ablakba (automatikusan nem lép át)
    print(browser.title)  # check, hogy tényleg ott vagyunk-e
    browser.close()  # bezárjuk

    browser.switch_to.window(main_window)  # vissza a főoldalra (automatikusan nem lép át)
    browser.close()

except:
    print("Valami hiba történt")

finally:
    browser.quit()


###  Window size  ################

try:
    browser.get(URL)

    browser.maximize_window()
    browser.set_window_size(500, 1000)  # ahhoz, hogy a gomb látszódjon, amit keresünk... át kell állítani a méretét
    time.sleep(2)

    toggle_btw = browser.find_element_by_xpath('//span[@class="navbar-toggler-icon"]')
    toggle_btw.click()
    print("Toggle btn is present")

except:
    print("Valami hiba történt")

finally:
    browser.quit()
