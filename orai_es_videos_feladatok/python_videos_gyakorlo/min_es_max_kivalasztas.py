# MINIMUM ÉS MAXIMUM KIVÁLASZTÁS
# SZÉLSŐÉRTÉK KERESÉS
# a legnagyobb és legkisebb szám megtalálása egy sorozatban

my_list = [2, 5, 8, 25, 111, 14, 1]
# hanyadik helyen van
# hanyadik helyen és melyik elem

max_element = my_list[0]
max_index = 0
for i in range(1, len(my_list)):  # azért az első elemtől, mert a nulladik már a max elementbe lett helyezve
    if my_list[i] > max_element:  # ha nagyobb az elem, mint a max
        max_element = my_list[i]  # akkor a max legyen egyenlő az elemmel
        max_index = i  # a max indexe legyen egyelő az elem indexével
print(max_index, max_element)

# egyszerűbb megoldás
max_element = my_list[0]
max_index = 0
for i, element in enumerate(my_list):  # azért az első elemtől, mert a nulladik már a max elementbe lett helyezve
    if element > max_element:  # ha nagyobb az elem, mint a max
        max_element = element  # akkor a max legyen egyenlő az elemmel
        max_index = i  # a max indexe legyen egyelő az elem indexével
print(max_index, max_element)


#  minimum kivalasztas
# egyszerűbb megoldás
min_element = my_list[0]
min_index = 0
for i, element in enumerate(my_list):  # azért az első elemtől, mert a nulladik már a max elementbe lett helyezve
    if element < min_element:  # ha nagyobb az elem, mint a max
        min_element = element  # akkor a max legyen egyenlő az elemmel
        min_index = i  # a max indexe legyen egyelő az elem indexével
print(min_index, min_element)