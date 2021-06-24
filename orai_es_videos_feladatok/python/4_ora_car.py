# Egy autokereskedes honlapjan vagyunk. Krealjunk egy menut, az alabbi menupontokkal:
# 1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.
# 2, Osszes kocsi adatai lekerdezese
# 3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)
# 4, Kocsi eladasa
# 5, Kilepes az applicaciobol


cars_name_list = []
cars_age_list = []
i = 0

while not (i == 5):
    print("Kocsi regisztrálása: 1 \n"
        "Összes kocsi adatainak lekérdezése 2 \n"
        "Adott kocsi adatainak lekérdezése (index alapján) 3 \n"
        "Kocsi eladása (törlése) 4 \n"
        "Kilépés a programból 5 \n")
    v = int(input("Válassz a fenti menüpontokból: "))
    if v == 1 or v == 2 or v == 3 or v == 4 or v == 5:
        i = v

    if i == 1:
        car_name = input("Kérlek add meg az autó nevét: ")
        car_age = input("Kérlek add meg az autó korát: ")
        cars_name_list.append(car_name)
        cars_age_list.append(car_age)
        i = 0

    if i == 2:
        j = 0
        while j < len(cars_age_list):
            print(cars_name_list[j], cars_age_list[j])
            j += 1

    if i == 3:
        j = int(input("kérlek add meg az indexét a megnézendő autónak: "))
        if j < len(cars_name_list):
            print(cars_name_list[j], cars_age_list[j])
        else:
            print("Nincs ilyen indexű autó")
            i = 3

    if i == 4:
        j = int(input("kérlek add meg az indexét az eladandó autónak: "))
        if j < len(cars_name_list):
            del cars_name_list[j]
            del cars_age_list[j]
        else:
            print("Nincs ilyen indexű autó")



