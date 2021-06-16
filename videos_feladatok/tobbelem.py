from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickybuttons.html")

    buttons = driver.find_elements_by_xpath('//button')  # s! beépített funkció, hogy az összes adott típust megtalálja
    print(buttons)  # terminálra kiírja, hogy miket talál
    print(type(buttons))  # terminálra kiírja, hogy milyen típusúak

    for button in buttons:  # for ciklussal bejárjuk a listában levő gombokat, majd mindre kattintunk
        button.click()
        result = driver.find_element_by_xpath('//label[@id="result"]')
        print(result.text)

        assert(result.text == f"{button.text} was clicked")  # a végén kiíratjuk a gombok feliíratait
finally:
    driver.close()
