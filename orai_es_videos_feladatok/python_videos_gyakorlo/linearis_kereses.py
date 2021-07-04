# LINEÁRIS KERESÉS
# ez valójában az eldöntés és a kiválasztás keveréke
# keressük meg az elemet a listában, ha létezik

my_list = [1, 5, 7, 11, 8, 25, 3]

index = 0
result = 0
while index < len(my_list) and my_list[index] < 20:  # addig megyek a ciklusban, amíg kisebb a szám 20-nál
    index += 1
if index < len(my_list):
    result = index  # az index (számot) átadjuk egy result változóba
print(result)


# for ciklussal kicsit pythonosabban
res = -1
for i in range(len(my_list)):
    if my_list[i] >= 20:
        res = i
        break
if res == -1:
    print("Nope")
else:
    print(res)