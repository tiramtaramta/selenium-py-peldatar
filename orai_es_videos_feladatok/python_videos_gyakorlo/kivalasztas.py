# KIVÁLASZTÁS
# Állapítsuk meg, hogy hol van a sorozatban egy adott tulajdonságú elem

my_list = ["alma", "korte", "barack", "citrom"]

index = 0
while my_list[index] != "barack":  # addig fusson, amíg az indexedik helyen levő elem nem egyenlő a stringgel
    index += 1
print(index)

# ugyanez for ciklussal
index = 0
for i, element in enumerate(my_list):  # enumerate az aktuális index és a hozzá tartozó elem
    if element == "barack":
        index = i
        break
print(index)

# for ciklussal még egyszerűbben
index = 0
for i in range(len(my_list)):
    if my_list[i] == "barack":
        index = i
        break
print(index)