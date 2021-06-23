from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # expected conditions neve az EC
from selenium.webdriver.support.wait import WebDriverWait


def check_xpath(str_url):
    bill_picture2 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, (str_url)))
    )
    return bill_picture2


PATH = "C:\\Windows\chromedriver.exe"
URL = "http://localhost:9999/general.html"
browser = webdriver.Chrome(PATH)
browser.maximize_window()


try:
    browser.get(URL)  # érdemes ide tenni a megnyitást
    bill_picture = check_xpath('//img[@src="https://www.fillmurray.com/402/295"]')
    print("Working")
except:
    print("Something went wrong!")
finally:
    browser.quit()
