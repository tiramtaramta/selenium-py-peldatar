"""
Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t ami csak az emailím és név oszlopokat tartalmazza.
"""

import csv

with open('table_in.csv') as csv_in:  # mit nyitunk meg, milyen változó néveel
    csv_reader = csv.reader(csv_in, delimiter=',')  # mi a file és mi az elválasztó
    # next(csv_reader)  # ez arra való, hogy a header sort ne olvassa be

    csv_list = []
    for row in csv_reader:  # soronként listába tesszük
        # print(row[0:2])
        csv_list.append(row)

with open('table_out.csv', "w", newline='') as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',')
    for line in csv_list:
        line = [x.strip() for x in line]
        csv_writer.writerow(line[1::-1])
