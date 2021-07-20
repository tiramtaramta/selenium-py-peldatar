from base_element import BaseElement  # base element file-ból importálunk
from selenium.webdriver.common.by import By


class TrainingGroundPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # a drivernek elkéri a get-jét és átadja az url-t
    def go(self):
        self.driver.get(self.url)

    def general_input(self, location_type, location_name):
        return BaseElement(driver=self.driver, by=location_type, value=location_name)

    @property
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    def close_test(self):
        self.driver.quit()
