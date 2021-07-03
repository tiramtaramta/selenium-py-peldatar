import csv

with open('petofi.txt', 'r', encoding="UTF-8") as petofi:
    word_list = petofi.read().split()
    new_list = []
    for index, value in enumerate(word_list):
        if (index + 1) % 2 == 0:  # ha a második szó, akkor ...
            if value[-1] == ",":  # ha vesszőre végződik a szó, akkor levágja
                value = value[:-1]
            row = (index + 1), value  # sorokban tároljuk a szó indexét és a szót
            new_list.append(row)

    with open('res.csv', "w", encoding="UTF-8", newline='') as res:
        csv_writer = csv.writer(res, delimiter=',')
        for row in new_list:
            csv_writer.writerow(row)