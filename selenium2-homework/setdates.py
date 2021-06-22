from datetime import datetime, date, time, timezone
from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(PATH)
browser.get(URL)

now_utc = datetime.now(timezone.utc)
# print(now_utc)
time.sleep(2)
browser.find_element_by_id("example-input-date").send_keys(now_utc.strftime("%Y.%m.%d"))
browser.find_element_by_id("example-input-date-time").send_keys(now_utc.strftime("%Y.%m.%d, %H:%M:%S:%f"))
browser.find_element_by_id("example-input-date-time-local").send_keys(now_utc.strftime("%Y/%m/%d,%I:%M,%p"))
browser.find_element_by_id("example-input-month").send_keys(now_utc.strftime("%Y.%B"))
browser.find_element_by_id("example-input-week").send_keys(now_utc.strftime("%W,%Y"))
browser.find_element_by_id("example-input-time").send_keys(now_utc.strftime("%I:%M,%p"))
# print(now_utc.strftime("%Y.%m.%d"))
# print(now_utc.strftime("%Y.%m.%d %H:%M:%S:%f"))
# print(now_utc.strftime("%Y/%m/%d,%I:%M,%p"))
# print(now_utc.strftime("%Y.%B"))
# print(now_utc.strftime("%W,%Y"))
# print(now_utc.strftime("%I:%M,%p"))

# browser.quit()
