class TrainingGroundPage:
    def __init__(self, driver, url):
        self.driver = driver  # a webdrivert fogjuk neki átadni
        self.url = url  # url-nek pedig a lenti url-t

    # a driver.get(url) segítségével beállítjuk az URL-t
    def go(self):
        self.driver.get(self.url)

    # kiválasztjuk az input mezőt, töröljü, majd beírjuk a text-et
    def type_int_input_field(self, text):
        input1 = self.driver.find_element_by_id('ipt1')
        input1.clear()
        input1.send_keys(text)
        return None  # ez nem kötelező sor, csak ezzel jelezzük, hogy nincs visszatérő értéke

    # kiválasztjuk ismét az input mezőt és lekérjük a value értékét (ellenőrzés céljából)
    def get_input_text(self):
        input1 = self.driver.find_element_by_id('ipt1')
        elem_text = input1.get_attribute('value')
        return elem_text

    # kiválasztjuk a gombot és klikkelünk
    def click_button_1(self):
        button1 = self.driver.find_element_by_id('b1')
        button1.click()
        return None

    def click_button_2(self):
        button2 = self.driver.find_element_by_id('b2')
        button2.click()
        return None

    # metódussal zárjuk be az oldalt
    def close_test(self):
        self.driver.quit()


# Our test
from selenium import webdriver

# Test Setup
input_value = "It worked"  # itt tároljuk a szöveget, amit a mezőbe írunk majd be
browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
URL = 'https://techstepacademy.com/training-ground'

# Test
# a class-t meghívva a tesztoldalra jelezzük, hogy a driver=browser, url=URL
test_page = TrainingGroundPage(driver=browser, url=URL)
test_page.go()  # itt meghívjuk a go metódust
test_page.type_int_input_field(input_value)  # a metódussal beírjuk az input_value-ba mentett szöveget
text_from_input = test_page.get_input_text()  # metódussal elkérjük azt a szöveget, amit beírtunk, hogy az assert lefusson

assert text_from_input == "It worked", f"Test Failed: Input did not match expected ({input_value})."
# szép megoldás az assertre -->
# assert text_from_input == "2", f"Test Failed: Input did not match expected ({input_value})."
test_page.click_button_1()  #a metódust meghívva kattintunk
test_page.close_test()  # a metódussal bezárjuk az oldalt

