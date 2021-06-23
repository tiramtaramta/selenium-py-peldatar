# comma-separated-valuse => csv
#csv.reader()
#csv.writer()

import csv

with open('data.csv') as csv_file:  # mit nyitunk meg, milyen változó néveel
    csv_reader = csv.reader(csv_file, delimiter=',')  # mi a file és mi az elválasztó
    next(csv_reader)  # ez arra való, hogy a header sort ne olvassa be
    for row in csv_reader:  # soronként listába tesszük
        print(row)