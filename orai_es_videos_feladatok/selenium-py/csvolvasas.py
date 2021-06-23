# comma-separated-valuse => csv
#csv.reader()
#csv.writer()

import csv

with open('data.csv') as csvfile:  # mit nyitunk meg, milyen változó néveel
    csvreader = csv.reader(csvfile, delimiter=',')  # mi a file és mi az elválasztó
    next(csvreader)  # ez arra való, hogy a header sort ne olvassa be
    for row in csvreader:  # soronként listába tesszük
        print(row)
