from datetime import datetime, date, time, timezone
from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

now_utc = datetime.now(timezone.utc)
print(now_utc)
#hh/nn/eeee formátumban
time.sleep(2)
browser.find_element_by_id("example-input-date").send_keys(now_utc.strftime("%Y/%m/%d"))

#browser.quit()
