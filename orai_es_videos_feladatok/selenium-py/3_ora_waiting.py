from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #expected conditions neve az EC
from selenium.webdriver.support.wait import WebDriverWait

#################### WAITING


def check_id(str_id):
    btn = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, (str_id)))
    )
    return btn


PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://webshop.progmasters.hu/"
browser = webdriver.Chrome(PATH)
browser.maximize_window()

try:
    browser.get(URL)
    login_btn = check_id("login")  #

    registration_btn = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'registration'))  # vár 5-öt, hogy megjelenjen a gomb
    )
    print("All good")
except TimeoutException as error:
    print(error, "Timeooooout")  ## ha valami nem stimmel, akkor tob egy timeout exception-t
    print("Something wrong")
finally:
    browser.quit()

