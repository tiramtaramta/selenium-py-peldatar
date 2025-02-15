import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from training_ground_page import TrainingGroundPage  # ha másik mappában van, akkor pelda2.training_ground_page...

input_value = "It worked"
browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
URL = 'https://techstepacademy.com/training-ground'

# lepéldányosítjuk az oldalt
test_page = TrainingGroundPage(driver=browser, url=URL)
test_page.go()

test_page.general_element(By.ID, "ipt1").send_text_to_input("Most egy probakor")
test_page.general_element(By.ID, "ipt2").send_text_to_input("Most meg egy probakor")
# test_page.input1().send_text_to_input("Most egy probakor")

assert test_page.general_element(By.ID, "b1").text() == 'Button1'
time.sleep(5)
test_page.close_test()
