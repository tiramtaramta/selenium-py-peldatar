"""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/pagination.html oldalt.
Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betüvel kezdődik.
A kiválasztott kontaktok összes adatát mentsd le memóriába egy szotár (dict) struktúrába.
Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.
"""

from selenium import webdriver
import time
import csv

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

            if cells[1].text.startswith("A"):
                extracted_data.append(data_row)  # objektumként hozzáadjuk az extracted_data listához

        next_button = browser.find_element_by_id("next")  # megkeressük a next gombot
        if not next_button.is_enabled():
            break  # ha a next button nem enabled (a lista végére értünk), akkor kilép a while ciklusból
        else:
            next_button.click()  # egyéb esetben pedig rákattintunk

    with open("pagination.csv", "w", newline='') as csv_pag:
        fieldnames = ["id", "first_name", "second_name", "surname", "second_surname", "birth_date"]  # mezőnevek
        csv_writer = csv.DictWriter(csv_pag, fieldnames=fieldnames)
        csv_writer.writeheader()  # kiírjuk a mezőneveket
        for row in extracted_data:
            csv_writer.writerow(row)  # soronként kiírjuk a találatokat

finally:
    browser.quit()