from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickibuttons.html")

    button2 = driver.find_element_by_xpath('//button[text()="button2"]')  # megkeressuk a button2-t
    button2.click() 

    result = driver.find_element_by_xpath('//label[@id="result"]')  # megkeressuk az eredményt
    print(result.text)

    assert(result.text == "button2 was clicked")
finally:
    driver.close()
