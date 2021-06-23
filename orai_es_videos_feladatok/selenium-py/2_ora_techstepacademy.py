from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://techstepacademy.com/trial-of-the-stones"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)

riddle_of_stone_input = browser.find_element_by_id("r1Input")
riddle_of_stone_input.send_keys("rock")
riddle_of_stone_btn = browser.find_element_by_id("r1Btn")
riddle_of_stone_btn.click()
element = browser.find_element_by_id("passwordBanner")
result1 = element.get_attribute('textContent')
# print(result1)

riddle_of_secret_input = browser.find_element_by_id("r2Input")
riddle_of_secret_input.send_keys(result1.strip())
riddle_of_secret_btn = browser.find_element_by_id("r2Butn")
riddle_of_secret_btn.click()

richest_merchant = browser.find_element_by_css_selector('#block-05ea3afedc551e378bdc > div > div:nth-child(18) > p')
richest_merchant_name = browser.find_element_by_css_selector('#block-05ea3afedc551e378bdc > div > div:nth-child(18) > span > b')
richest_input_name = richest_merchant_name.get_attribute('textContent')
richest_input_field = browser.find_element_by_id('r3Input')
richest_input_field.send_keys(richest_input_name)
richest_btn = browser.find_element_by_id("r3Butn")
richest_btn.click()

success = browser.find_element_by_id('checkButn')
success.click()

trial_complete = browser.find_element_by_id("trialCompleteBanner")
print(trial_complete.text)