# a hosszú oldalakon belüli scrollozás lehetősége
# lehet anchor linkek alapján (ez volt korábban a navigatio.py file-ban)
# lehet page down és end gombok alapján is le fel ugrálni az oldalon
# valamint javascript segítségével akár az oldal aljára, vagy egy megadott magasságra is

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/general.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    # egyik opció
    html = browser.find_element_by_tag_name("html")  # html tag-et kiemelem, ami az egész oldalt tartalmazza (képernyőn kívülit is)
    html.send_keys(Keys.END)  # ezzel lemegyünk az oldal aljára

    # második opció javascript segítségével
    # js = "window.scrollTo(0, document.body.scrollHeight);"  # az ablakot tessék lescrollozni az y-on egészen az aljára
    # js = "window.scrollTo(0, 2000);"  # egyéb érték is megadható
    # browser.execute_script(js)


finally:
    pass
    # browser.quit()