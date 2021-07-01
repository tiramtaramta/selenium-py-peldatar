from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    # egyből mentsük el az ablakok referenciáját
    main_window = browser.window_handles[0]
    browser.execute_script("window.open('', 'newwin', 'height=800,width=600')")  # egy kis js az új ablak beállításához
    new_window = browser.window_handles[1]  # ezt még nem nyitottuk meg, csak eltároltuk

    browser.switch_to.window(new_window)  # lépjünk át az új ablakba
    browser.get("http://localhost:9999/general.html")  # megmondjuk, hogy az új ablakban mi nyíljon meg
    text = browser.find_element_by_tag_name("h4").text  # kikeressük a megfelelő szövegrészt

    browser.switch_to.window(main_window)  # visszaváltunk az eredeti ablakba
    example_input = browser.find_element_by_id("example-input-text")  # egy példa beviteli mező kiválasztása
    example_input.send_keys(text)  # belehelyezzük a másik oldalról kimentett szövegrészt
except:
    print("Valami hiba történt")
finally:
    pass
    # browser.quit()