from selenium import webdriver

# PATH = "C:\\Windows\\chromedriver.exe"
#
# browser = webdriver.Chrome(PATH)
#
# browser.get("https://www.google.com")
# print(browser.title)  # írja ki az oldal nevét
# browser.quit()  # ez is bezáró parancs, mt a close


PATH = "C:\\Windows\\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get("https://www.index.hu")
browser.save_screenshot("screenshot.png")  # screenshot-ot készít az ablakról
browser.quit()