"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. 
A program töltse be a példatárból az http://localhost:9999 oldalt. Lokátorral keresd ki az összes linket az oldalról. 
Tárold a memóriában egy listában az összes linket. A list tartalmát írd ki egy fájlba. Minden link egy új sorba kerüljön. 
A kimenetre írd ki hány linket találtál
"""
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"

browser = webdriver.Chrome(PATH)


def file_write():
    with open("links.txt", "w") as file:
        for link in links_list:
            file.write(link + "\n")
        file.close()


def count_links():
    list_len = len(links_list)
    print(list_len)


try:
    browser.get("http://localhost:9999")

    links = browser.find_elements_by_xpath("//a[@href]")
    links_list = []

    if len(links) > 0:
        for link in links:
            links_list.append(link.get_attribute("href"))
    else:
        print("Nincsenek linkek az oldalon.")

    file_write()
    count_links()

finally:
    browser.quit()


### Kocka megoldása
# from selenium import webdriver
#
# PATH = "D:\Progmasters\Python-basics\webdriver\chromedriver.exe"
# URL = "http://localhost:9999"
#
# browser = webdriver.Chrome(PATH)
# browser.get(URL)
#
# link_list = browser.find_elements_by_css_selector('a')
# href_link = []
# for i in link_list:
#     href_link.append(i.get_attribute("href"))
# browser.quit()
#
# my_link_writing = open('links.txt', 'a')
#
# for i in href_link:
#     my_link_writing.write(i)
#     my_link_writing.write("\n")
#
# my_link_writing.close()
# my_link_read = open("links.txt", 'r')
# txt_content = my_link_read.read()
# my_link_read.close()
# print(txt_content, len(href_link))