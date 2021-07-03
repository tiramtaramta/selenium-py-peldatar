from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/general.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    browser.maximize_window()  # fontos beállítani a képernyő méretét!

    # szebb, ha egyenként kigyűjtjük az elemeket és csak  utána hajtunk végre feladatokat velük
    login_menu_btn = browser.find_element_by_id("login")
    login_menu_btn.click()

    email_input = browser.find_element_by_id("email")
    password_input = browser.find_element_by_id("password")
    login_btn = browser.find_element_by_xpath('//button[@type="submit"]')

    email_input.send_keys("admin1@gmail.com")
    password_input.send_keys("admin21")
    login_btn.click()


    paragraph_block = browser.find_element_by_id("phrasing")  # id-val mindig egy db objektumot választhatunk (nincs mozgástér)

    bill_picture = browser.find_element_by_xpath('//img[@src="https://www.fillmurray.com/402/295"]')
    # xpath esetén ki-be tudunk mozogni az elemeknél $x('//img') == $x('//img[@src="https://www.fillmurray.com/402/295"]')

    figure_block = browser.find_element_by_xpath('//img[@src="https://www.fillmurray.com/402/295"]/..')
    # /.. egyet kiugrunk vele a hierachiában

    figcaption = browser.find_element_by_xpath('//img[@src="https://www.fillmurray.com/402/295"]/../figcaption')
    # /../figcaption-nel a figure blokkban választunk ki egy másik elemet a

    figcaption2 = browser.find_element_by_xpath('//figcaption[text()="Figure 1: A picture of Bill Murray from "]')
    # direktben is elérhető, ha megmondjuk a text tartalmát pontosan (de ha bármi változik, már nem fog működni)!

except:
    print("Something went wrong")

finally:
    browser.quit()
