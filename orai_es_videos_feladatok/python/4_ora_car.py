# Egy autokereskedes honlapjan vagyunk. Krealjunk egy menut, az alabbi menupontokkal:
# 1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.
# 2, Osszes kocsi adatai lekerdezese
# 3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)
# 4, Kocsi eladasa
# 5, Kilepes az applicaciobol


car_type_list = []
car_age_list = []
i = 0

while not (i == 5):
    print("Kocsi regisztrálása: 1-es gomb \n"
        "Összes kocsi adatainak lekérdezése: 2-es gomb \n"
        "Adott kocsi adatainak lekérdezése (index alapján): 3-as gomb \n"
        "Kocsi eladása (törlése): 4-es gomb \n"
        "Kilépés a programból: 5-ös gomb \n")
    v = int(input("Válassz a fenti menüpontokból: "))
    if v == 1 or v == 2 or v == 3 or v == 4 or v == 5:
        i = v

    if i == 1:
        car_type = input("Kérlek add meg az autó típusát: ")
        car_age = input("Kérlek add meg az autó korát: ")
        car_type_list.append(car_type)
        car_age_list.append(car_age)
        i = 0

    if i == 2:
        j = 0
        while j < len(car_age_list):
            print(car_type_list[j], car_age_list[j])
            j += 1

    if i == 3:
        j = int(input("Kérlek add meg az indexét a megnézendő autónak: "))
        if j < len(car_type_list):
            print(car_type_list[j], car_age_list[j])
        else:
            print("Nincs ilyen indexű autó")
            i = 3

    if i == 4:
        j = int(input("Kérlek add meg az indexét az eladandó autónak: "))
        if j < len(car_type_list):
            del car_type_list[j]
            del car_age_list[j]
        else:
            print("Nincs ilyen indexű autó")
            break
            i = 4





