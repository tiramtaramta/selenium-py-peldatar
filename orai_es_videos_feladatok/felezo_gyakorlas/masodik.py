from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://happy-sea-0a5ffef03.azurestaticapps.net/masodik.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    browser.maximize_window()

    def print_todo_list():
        todos_list = browser.find_elements_by_xpath('//*[@id="container"]/ul/li')  # listában tároljuk a todos elemeit
        for todo in todos_list:
            print(todo.text)

    add_new_todo = browser.find_element_by_xpath('//*[@id="container"]/input')
    delete_todo = browser.find_element_by_xpath('//*[@id="container"]/ul/li[1]/span/i')

    add_new_todo.send_keys("Newest Todo")  # beírjuk a beviteli mezőbe
    add_new_todo.send_keys(Keys.ENTER)  # majd entert nyomunk

    time.sleep(4)
    print_todo_list()  #printeljük, hogy hozzáadódott-e

    delete_todo.click()
    time.sleep(2)
    print_todo_list()  # törlés után ismét printeljük, hogy törlődött-e elem

except:
    print("Valami elromlott")

finally:
    browser.quit()

# Kocka megoldás
# try:
#     browser.get(URL)
#
#
#     def print_todo_list():
#         todos_list = browser.find_elements_by_xpath('//*[@id="container"]/ul/li')  # listában tároljuk a todos elemeit
#         for todo in todos_list:
#             print(todo.text)
#
#     browser.maximize_window()
#     add_new_todo = browser.find_element_by_xpath('//input[@placeholder="Add new todo"]')
#     delete_todo = browser.find_elements_by_xpath('//i[@class="fa fa-trash"]')[0]  # lista nulladik elemét kérjük le
#
#     add_new_todo.send_keys("Newest Todo")  # beírjuk a beviteli mezőbe
#     add_new_todo.send_keys(Keys.ENTER)  # majd entert nyomunk
#
#     time.sleep(4)
#     print_todo_list()  #printeljük, hogy hozzáadódott-e
#
#     delete_todo.click()
#     time.sleep(2)
#     print_todo_list()  # törlés után ismét printeljük, hogy törlődött-e elem
#
# except:
#     print("Valami elromlott")
#
# finally:
#     browser.quit()
