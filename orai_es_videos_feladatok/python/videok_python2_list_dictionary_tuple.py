"""
összetett adattípusok bevezető
"""

###################### lista típus (List)#####################
# A lista egy összetett adattípus (heterogén gyűjtemény)

my_list = [1, 2, 3]  # homogén gyűjtemény, ha egyféle adattípus van benne
my_list2 = [1, "leves", 6, True]  # heterogén gyűjtemény

# lista hosszának lekérdezése
print(len(my_list2))

### NESTED list (ágyazott listák)
my_nested_list = [1, 2, [1, 2], "alma", True]

### lista elemének elérése (0 indextől)
my_list3 = [1, 2, 3, 4, "alma"]
print(my_list3[0])  # a lista nulladik elemét szeretném elérni

print(my_list3[-1])  # ismeretlen hosszúságú lista utolsó elemének kiíratása

print(my_list3[8])  # nem létező index  ==>  list index out of range

################ listák metódusai #######################

### lista hosszának lekérdezése              LEN
my_len = len(my_list3)
print(my_len)

my_list4 = []
it_length = int(input())
for i in range(it_length):
    my_list4.append(i)

print(len(my_list4))

### lista elem tartalmának lekérdezése         IN
fruits = ["alma", "körte", "banan"]

print("citrom" in fruits)  # False
print("alma" in fruits)  # True

# példa:
fruits2 = ["alma", "körte", "banan"]
my_fruit = input()
print(my_fruit in fruits2)

### lista műveletek Csak ez a kettő
a = [1, 2, 3]
b = [5, 6]

### concatenálás (összefűzés)
c = a + b
print(c)

### (szorzás)
c = a * 3
print(c)

#### lista elemének módosítása
my_list5 = [1, 2, 3]
print(my_list5)

my_list5[0] = "alma"  # indexxel megadva cserélhető az elem
print(my_list5)

my_list5[3] = "alma"  # ilyen indexű elem nem létezik, így nem cserélhető

### lista vágása            SLICE
# a lista elejének vágása másolatba
my_list6 = [1, 2, 3, "alma", "körte", 3.14]
my_sliced_list = my_list6[0:3]  # a 0-tól a harmadik elemig vágódik le a
# my_sliced_list = my_list6[:3]  # egyszerűsített írás
print(my_sliced_list)

### a lista végének vágása másolatba
my_sliced_list2 = my_list6[3:]  # 4. elemtől (3. indextől a végéig)
print(my_sliced_list2)

# a lista másolata
my_sliced_list3 = my_list6[:]  # ez az egész listát lemásolja
print(my_sliced_list3)

### lista elemének törlése           DEL
# a konkrét listából törlés (nem másolatból!!!)
my_list7 = [1, 2, 3, "alma", "körte", 3.14]
print(my_list7)
del my_list7[3]  # a 3-as indexű elemet törlöm
print(my_list7)
del my_list7[0:3] # az első 3 indexű elemet törli a listából


### lista használata számláló ciklusban
my_list8 = [4, 55, 23, 2]
for i in range(len(my_list8)):
    print(i, my_list8[i])

for (i, v) in enumerate(my_list8):    # ENUMERATE
    print(i, v)

### lista, mint függvény paramétere


def foo2(a_list):
    new_list = a_list[:]
    for (i, v) in enumerate(a_list):  # ENUMERATE
        new_list[i] = 2 * v  # megduplázza az értékeket és új listaként adja vissza
    return new_list


my_list9 = [1, 2, 3, 4, 5]
print(my_list9)
return_list = foo2(my_list9)
print(my_list9)
print(return_list)


### lista beépített függvényei
my_list = []
my_list[0] = 12  #
my_list.append(12)
my_list.insert(0, 12)  # hova és mit (ha már van nulladik, akkor azt tolja az 1-re
print(len(my_list))  # lsita hossza
print(my_list.count(12))  # megszámolja, hogy hány 12-es van a listában
my_list.extend([8, 9])  # a lista bővítése
my_list.reverse()  # a lista megfordítása
my_list.short()  # a lista nagyságrendbe rendezése
del my_list[0]  # a lista 0. elemének törlése
my_list.remove(12)  # törli az első előfordulását a 12-nek


### listába ágyazott lista
my_map = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
for i in my_map:
    for j in i:
        print(j)  # 12345678

print(my_map[0])  # [0, 1, 2]
print(my_map[0][1])  # 1


### listák és karakterláncok kapcsolata
my_string = "Hello World"
print(my_string.split(" "))  # ['Hello', 'World"]
num_of_words = my_string.split(" ")
print(num_of_words)  # 2

fruits3 = ["alma", "korte", "barack"]
print(" ".join(fruits))  # alma korte barck
print(", ".join(fruits))  # alma, korte, barck

## lista feladat... karakterlánc keresése
my_list10 = ["almaxxx", "xxx", "korte", "banxxxan", 12, "yyy"]
my_count = 0
for element in my_list10:
    if type(element) != str:  # ha az elem nem string
        continue
    if "xxx" in element:  # ha az xxx benne van az elemben
        my_count += 1
print(my_count)


############## Rekordok TUPLE ###################

my_record = ("Pete", 1985)
# my_record = tuple("Pete", 1985, "alma") nem fontos a tuple-t kiírni
print(my_record[0])
# my_record[0] = "X"  # NEM MÓDOSÍTHATÓ

#pl.:


def foo():
    return 1, 2  # nem szabad zárójelbe tenni


print(type(foo()))

#### record (tuple) listává alakítása
my_record2 = ("Pete", 22, "körte")
my_list8 = list(my_record2)
my_list8.append("x")  # listává alakítás után már lehet hozzáfűzni adatot
print(my_list8)

############## szótár (dictionary) #####################
# összerendelési típus, kulcsokról és hozzájuk tartozó értékekről szól
# nincs köztük sorrend!!!
my_list9 = [1, 2, 3]
my_dict = {"alma": 1, "körte": 12, 1: 3.14}
my_dict2 = dict()  # így is létrehozható
print(my_dict)

#### szótár elem elérése

my_dict3 = {"alma": 1, "körte": 12, 1: 3.14}
print(my_dict3["alma"])  # ==> kiírja az 1-est

if "1" in my_dict3:
    print(my_dict3["1"])  # ==> key error, ha olyan kulcsra hivatkozunk, ami nem létezik
    # így nem kapunk hibát, mert az in megnézni, hogy van e

### szótár elem törlése
del my_dict3["alma"]  # törli az alma kulcsú értéket és a kulcsot is
print(my_dict3)

### szótár elem módosítása
my_dict4 = {"alma": 1, "körte": 12, 1: 3.14}
print(my_dict4)
my_dict4["alma"] += 5  # az alma kulcsú érték növelődik 5-tel
print(my_dict4)

### szótárak beépített metódusai
# for ciklussal végigjárni a dictionary-t

for i in my_dict3:  # az értékeket írja ki
    print(i)

for i in my_dict3.keys():  # ezzel a kulcsokon megyünk végig
    print(i)

for i in my_dict3.values():  # ezzel az értékeken megyünk végig
    print(i)

for k, v in my_dict3.items():  # ezzel a kulcsokon és az értékeken is végigmegyünk
    print(k, v)

### szótár listává alakítása
my_list10 = list(my_dict4.keys())  # a kulcsok listába másolása
my_list10 = list(my_dict4.values())  # az értékek listába másolása