from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

try:
    browser.get("http://localhost:9999/kitchensink.html")

    # display: none nem jelenik meg
    # visibility: hidden fenntartja a helyét, csak nem látszik
    # a hide/show example részben tesztelünk

    input_text = browser.find_element_by_id("displayed-text")
    hide_button = browser.find_element_by_id("hide-textbox")
    show_button = browser.find_element_by_id("show-textbox")
    print(input_text.is_displayed())  # mit lát a selenium? látszik-e enabled, displayed, selected?
    hide_button.click()
    print(input_text.is_displayed())  # első esetben True, másodikban False

    # input_text.is.displayed fontos vizsgálati elem. Kiderül, hogy meg tudom-e nyomni
    # .is.selected kiválasztással meg tudjuk nézni, hogy ki van-e választva a gomb


finally:
    browser.quit()