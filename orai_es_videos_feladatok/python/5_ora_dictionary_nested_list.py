###### DICTIONARY - szótár

# Mi a szótár? Speciális tároló, ami (key-value)kulcs-érték párokat tartalmaz.
# A kulcsnak egyedinek (unique) kell lennie.
# dictionary-t leginkább arra használjuk, hogy megszámoljuk, hány darab van benne

person = {
    "name": "Keith",
    "age": 20,
    "address": "USA"
}

# üres szótár létrehozása:
my_dictionary = dict()

# Ki tudjuk íratni az értékeket a kulcsok meghívásával.
print(person["name"])  # Keith
print(person["age"])  # 20
#
print(person.keys())  # name, age, address egy dictionary listában
print(person.values())  #  Keith, 20, USA egy dictionary listában

# Értékek felülírása
print(person["age"])  # eredeti érték kiírása
print(person.get("age"))  # Eredeti érték kiírása .get metódussal
person["age"] = 100
print(person.get("age"))  # Felülírt érték kiírása .get metódussal


########################### lekérdezések

# Hogyan használhatunk loopokat a dictionary-n?
# Kulcsok lekérdezése
for key in person:
    print(key)

# kulcsok lekérdezése szebb megoldással (egyértelműbb)
for i in person.keys():
    print(i)

# értékek lekérdezése
for i in person.values():
    print(i)

# Kulcs és érték kiíratása
for i in person:
    print(i, person[i])  # kiírja a kulcsokat alapértelmezetten, plusz az i-edik értéket is

# kulcs és érték kiírása egész mondatban
for i in person:
    print(f" Person {i}, Value: {person[i]}")

# kulcs és érték kiírása .items() függvénnyel
for key, value in person.items():
    print(key, value)


# Érték felülírása
person["age"] += 2
person["address"] = "Canada"
print(person)

# Új kulcs - érték hozzáadása:
person["hair_color"] = "black"  # pont mint az update... ha már létezik, felülírja
print(person)

# Elem törlése (kulcs-érték)
del person["address"]
print(person)

# törli a kulcs-érték párokat a dictionary-ból (üres lesz)
person.clear()
print(person)

# dictionary teljes törlése
del person



###### NESTED LIST

my_map = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

my_map2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# elem hozzáadása
my_map.append([10, 11, 12])
print(my_map)

# elem törlése
del my_map[0]
print(my_map)

#  For ciklussal tudjuk kiíratni a listákat
for i in my_map:
    print(i)  # [1, 2, 3], [4, ...

#  Egymásba ágyazott for ciklussal tudjuk bejárni a nested list-et
for i in my_map:
    for k in i:
        print(k)  # 1, 2, 3, 4, 5, 6, ...

# 0. elem lekérdezése
print(my_map[0])

#  A második elem 0. indexű értékét
print(my_map[1][0])

friend_list = [["Joey", "Phoebe"], ["Rachel", "Ross"], ["Monica", "Chandler"], ["Gunther"]]
# Access for a specific element in the nested list. Let's get Ross Eustace Geller!
print(friend_list[1][1])