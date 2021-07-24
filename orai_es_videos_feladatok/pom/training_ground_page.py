from base_element import BaseElement  # base element file-ból importálunk
from selenium.webdriver.common.by import By

# lepéldányosítjuk magát a honlapot
class TrainingGroundPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # a drivernek elkéri a get-jét és átadja az url-t
    def go(self):
        self.driver.get(self.url)

    # ezzel bármilyen element leképezhető és a tesztben csak a (By.ID, "ipt1") kell mellé
    def general_element(self, location_type, location_name):
        return BaseElement(driver=self.driver, by=location_type, value=location_name)

    # # ha így lenne minden elemre megírva, akkor nem kell a zárójel, amikor példányosítom a pom testben
    # @property
    # def input1(self):
    #     locator = (By.ID, "ipt1")
    #     return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    def close_test(self):
        self.driver.quit()
