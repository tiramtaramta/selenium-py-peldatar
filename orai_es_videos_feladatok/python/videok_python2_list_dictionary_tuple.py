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