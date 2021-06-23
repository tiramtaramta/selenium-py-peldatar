from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/general.html"
browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

"""
egy adott code elérése xpath-szal ==> $x('//code[text()="samp"]')[0]
ha az adott kód egész bekezdését kell kiválasztani ==> $x('//code[text()="samp"]/..')[0]
ha további elemhez szeretnénk feljebb ugrani ==> $x('//code[text()="samp"]/../..')[0]
"""

my_samp = browser.find_elements_by_xpath('//code[text()="samp"]')[0]  # $x('//code[text()="samp"]')[0]
print(my_samp.text)  #a my samp element szövegét printeli ki

browser.quit()
