# a lapozó felületek esetében sokszor nincs új adatbetöltés, hanem ajax keretrendszer, csak lecseréli
# a végtelen adatkinyerés megvalósítható, ha vannak következő és előző gombok is

from selenium import webdriver
import pprint
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/pagination.html"

browser = webdriver.Chrome(PATH)

extracted_data = []  # létrehozunk egy üres listát a kicsomagolt adatoknak

try:
    browser.get(URL)
    while True:  # betesszük egy végtelen ciklusba, ami addig fut, amíg a break le nem állítja
        time.sleep(2)  # ez csak azért kell bele, hogy szemmel is követni lehessen
        table = browser.find_element_by_xpath("//table[@id='contacts-table']/tbody")  # tábla kiválasztása
        rows = table.find_elements_by_tag_name("tr")  # a tábla sora egy tr-nek felel meg
        for row in rows:
            data_row = {}  # soronként beolvassuk egy dictionary-be
            cells = row.find_elements_by_tag_name("td")  # a cella egy td elemnek felel meg
            data_row["id"] = cells[0].text  # beolvasás a data_row dictionary-be (kulcs és a cella textje a value
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)  # objektumként hozzáadjuk az extracted_data listához

        next_button = browser.find_element_by_id("next")  # megkeressük a next gombot
        if not next_button.is_enabled():
            break  # ha a next button nem enabled (a lista végére értünk), akkor kilép a while ciklusból
        else:
            next_button.click()  # egyéb esetben pedig rákattintunk
    pprint.pprint(extracted_data)  # kiíratjuk az objektumokat
    print(len(extracted_data))  # kiíratjuk a lista hosszát


finally:
    browser.quit()