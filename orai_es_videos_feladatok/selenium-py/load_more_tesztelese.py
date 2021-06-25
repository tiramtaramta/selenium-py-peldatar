# a legprimitívebb megoldása egy ajaxos gomb
# amire használhatjuk: hogy beolvasunk adatokat az újabb megjelenő elemekből

from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/loadmore.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    # xpath megfogalmazása = keressünk bárhol az oldalon // egy olyan divet, minek a class-a load-more-button
    # és ezen belül / az első gomb
    load_more = browser.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(5):  # kattintsunk 5x a load more gombra
        time.sleep(3)
        images = browser.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:  # az utolsó 5 elemnek az értékét kérjük csak el, mert különben redundáns lesz
            print(j.find_element_by_tag_name("img").get_attribute("src"))  # img scr-t íratjuk ki
            print(j.find_element_by_tag_name("p").text)  # és a kép p tag-jében található szöveget íratjuk ki
        load_more.click()
        # ha az összes elemre szükség van, akkor egy végtelen ciklusba be lehet tenni az egészet
        # és csak a load_more gombot kell megvizsgálni kattintás előtt,
        # hogy is not enabled (nem elérhető), vagy disabled (kikapcsolt) és akkor break utasítással leállítható,
        # mint a lapozó esetében
finally:
    browser.quit()