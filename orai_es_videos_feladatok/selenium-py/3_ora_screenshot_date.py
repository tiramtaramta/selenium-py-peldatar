import datetime
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("http://www.444.hu")

capture_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # lekérdezzük az időt és formázzuk
driver.save_screenshot("capture_" + capture_time + ".png")  # milyen néven mentsük el
driver.close()
