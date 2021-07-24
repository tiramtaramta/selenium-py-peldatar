from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ezen az oldalon írjuk meg a seleniumos kódokat
class BaseElement(object):  # itt kötelező berakni, hogy object
    def __init__(self, driver, by, value):
        self.driver = driver  #
        self.by = by  # mi alapján keresünk elemet
        self.value = value  # mit keresünk
        self.locator = (self.by, self.value)  # itt hozzuk létre a locatort a by és a value értékekkel
        self.web_element = None  # web elementet beállítjuk none-ra, mert később adjuk át neki a többi értéket
        self.find()  # a fenti elemekből ő gyártja le

    # vár 10 mp-et, majd összeszedi a locator alapján az értékeket és összerakja a web_elementet (ami fent none)
    def find(self):
        self.web_element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))

    def send_text_to_input(self, text):
        self.web_element.send_keys(text)
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    # a gomb text-jét így kérjük el
    def text(self):
        text = self.web_element.text
        return text
