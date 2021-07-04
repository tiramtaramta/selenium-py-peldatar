# ELDÖNTÉS
# 1. Állapítsuk meg, hogy van-e a sorozatban adott tulajdonságú elem
# visszatérési érték boolean
my_list = [3, 6, 5, 11, 23]
index = 0
while index < len(my_list) and my_list[index] < 10:
    index += 1  # a lista utolsó eleme után is növelünk egyet az indexen, így meg fog egyezni a my_list hosszával
print(index)
print(index < len(my_list))

# egyszerűbb megoldás pythonosan
is_ok = False  # alapból false az értéke
for element in my_list:
    if element > 10:  # ha van benne 10-nél nagyobb elem, akkor True-ra állítjuk
        is_ok = True
        break
print(is_ok)

# 2.  Állapítsuk meg, hogy a sorozatban MINDEN elem adott tulajdonságú-e
index = 0
while index < len(my_list) and my_list[index] > 10:
    index += 1  # a lista utolsó eleme után is növelünk egyet az indexen, így meg fog egyezni a my_list hosszával
print(index)
print(index == len(my_list))

# egyszerűbb megoldás pythonosan
is_ok = True  # alapból true az értéke
for element in my_list:
    if element <= 10:  # ha van benne 10-nél nagyobb elem, akkor True-ra állítjuk
        is_ok = False
        break
print(is_ok)