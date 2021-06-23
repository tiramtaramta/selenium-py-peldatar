from selenium import webdriver

# PATH = "C:\\Windows\\chromedriver.exe" # Másik megoldás, ami elegánsabb
# browser = webdriver.Chrome(PATH)

driver = webdriver.Chrome()

driver.get("https://python.org")

q = driver.find_element_by_name("q")
q.send_keys("input")

submit = driver.find_element_by_name("submit")
submit.click()

#driver.close()