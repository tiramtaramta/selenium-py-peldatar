# and és or feltételek logikai értelmezése
name = "Rolf"
drink = "Beer"
food = "Burger"

if name == "Rolf" and drink == "Beer" and food == "Burger":
    print("AND")
elif name == "Rolf" or (drink == "Beer" and food == "Burger"):
    print("OR / and1")
elif name == ("Rolf" and drink == "Beer") or food == "Burger":
    print("OR / and2")
else:
    print("Else")


"""
listák darabolása slice

"""
cars = ["Audi", "Trabant", "Bmw", "Tesla", "Ford", "Ferrari"]

# Ez a lista második (1) és a harmadik (2) elemet listázza ki (trabant és bmw.
sliced_car1 = cars[1:3]
print(sliced_car1)

# Ez a lisa 2-es indexű elemétől írja ki:
sliced_car2 = cars[2:]
print(sliced_car2)

# Ez az lista 3-as indexű eleméig írja ki
sliced_car3 = cars[:3]
print(sliced_car3)


# az utolsó két elemet adja vissza
sliced_car4 = cars[-2:]
print("From back to end: " + str(sliced_car4))

# az utolsó két elemet kivételével adja vissza
sliced_car5 = cars[:-2]
print("From front to back " + str(sliced_car5))

# a lista másolása
copy_list = cars[:]
copy_list.append("Kutyakutya")  # másolt listához hozzáadás
print(copy_list)

for i in cars[2:]:  # meg lehet adni a for ciklusban, hogy hanyadik elemtől mendjen végig
    print(i)

# Ez a slice ugyanúgy működik a stringeknél is

# első elem levágása
my_str = "Kutya"
print(my_str[1:])

our_string = "DogCatMouse"
sliced_string = our_string[2:len(our_string) - 2]  # 2. indextől a hossz -2 ig vágjuk le
sliced_string2 = our_string[2:9]
print(sliced_string)
print(sliced_string2)


"""
Beépített funkciók
"""

word = "Hello"
print(word.upper())  # nagybetűs
print(word.lower())  # kisbetűs
print(word.capitalize())  # kiskapitális
print("Hello".startswith("h"))  # kis kezdőbetűs? false
print("Hello".startswith("H"))  # nagy kezdőbetűs? true
print("Hello".endswith("O"))  # nagy utolsóbetűs? false
print("Hello".endswith("o"))  # kis utolsóbetűs? true


"""
hasznos lista funkciók a python library-ban
"""

# minimum és maximum kiválasztás csak integerrel működik
numbers_list = [3, 2, 2, 50, -20, -30]
a = min(numbers_list)  # minimum kiválasztás (stringgel abc-be rendezi)
b = max(numbers_list)  # maximum kiválasztás
# print(min(numbers_list))  # rövidebb kódsorban
print(a)
print(b)

# szum függvény csak integerrel működik
total = sum(numbers_list)
print(numbers_list)

# növekvő sorrendbe teszi a lista értékeit a .sort()
numbers_list.sort()
print(numbers_list)
#
# megfordítja a lista eredeti sorrendjét .reverse()
numbers_list.reverse()
print(numbers_list)

# lista csökkenő sorrendbe rendezi a listát
numbers_list.reverse(numbers_list.sort())
print(numbers_list)

# listához új elem hozzáadása (csak a végére lehet)
numbers_list.append(1000)
print(numbers_list)

# # a lista teljes ürítése
# numbers_list.clear()
# print(len(numbers_list))  # így nézzük meg a lista hosszát

# lista bővítése
list2 = [1, 50, 60]
numbers_list.extend(list2)  # tömb a tömbben
print(numbers_list)

# elem eltávolítása a listából /// stringeknél is működik
numbers_list.remove(2)  # nem index alapján, hanem érték alapján nézi és a lista első 2-esét törli a listából
print(numbers_list)

string_list = ["kutya", "cica", "cica"]
string_list.remove("cica")  # nem index alapján, hanem érték alapján nézi és a lista első cicáját törli a listából
print(string_list)

# a legutolsó elem törlése a listából
numbers_list.pop()
print(numbers_list)

# első elem törlése a listából
numbers_list.pop(0)
print(numbers_list)

# pythonos törlés index alapján
del numbers_list[1]
print(numbers_list)

# törlés tól-ig index alapján
del numbers_list[0:3]
print(numbers_list)

# törlés a hosszának a feléig
del numbers_list[0:(int(len(numbers_list) / 2))]
print(numbers_list)

# megszámolja, hogy az adott elemből hány fordul elő a listában
how_mutch = numbers_list.count(2)
print(how_mutch)


"""
CREATE function - Saját metódus készítése
"""


def add_two_number(a, b):  # definiálunk egy funkciót
    print(a + b)


add_two_number(2, 3)  # majd meghívjuk a konkrét értékekkel
add_two_number(5, 6)

##################################


def print_cica():
    print("Cica")


print_cica()

####################################
age = 18
age2 = 17


def check_age(parameter):
    if parameter < 18:
        print("You are under aged")
    else:
        print("You are an adult")


check_age(age)
check_age(age2)

# ugyanez metódus nélkül
# age = 18
# age2 = 17
# if age < 18:
#     print('You are under aged')
# else:
#     print('You are an adult')
#
# if age2 < 18:
#     print('You are under aged')
# else:
#     print('You are an adult')

###################################


def greet(name, default_age = 0):
    print(f"Hello, my name is {name} and I am {default_age} years old")


greet("Jamal", 5)  # két értékkel a default age felülíródik
greet("Monica")   # egy értékkel az alapértelmezett jelenik meg


"""
Try exception - kivételkezelés
"""

# Two type of error exist in Python.
# 1, Syntax error: When you want to start your program and interpreter gonna drop this error.
# Application stops immediately. You wrote a piece of code that interpreter can not understand.
# 2, Exceptions: Piece of code which Syntactically good, but something went wrong
# and it does something else then you were expected.
# It also stops the application if you dont handle the problem. More type exists.

# SyntaxError: / ezeket nem lehet lekezelni, figyelni kell rá
print("1")
print("2")
# print(3")
#
# # Example for Exceptions:
# # ZeroDivisionError: division by zero  / nullával való osztás
print(10 * (1 / 0))
#
# # NameError: name 'dog' is not defined  / nincs a dog definiálva
# 4 + dog * 3
#
# #TypeError: can only concatenate str (not "int") to str  / stringet és intet nem tud összeadni
print('2' + 2)

# példa
try:
    print('2' + 2)
except:
    print("Hiba a kódban")

# példa a hibák pontosítására
try:
    print('2' + 2)
except NameError:
    print("Hiba a névben")
except TypeError:
    print("Hiba a rendszerben")
finally:
    print("Ez az ág mindenképpen lefut")
print("itt is tovább fut")

#  How we catch/ handle this errors?  We can use a try/except block.
# This except going to handle all kind of Error, no matter what it is.
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Denominator can not be 0")
except ValueError:
    print("Please use numbers!")
finally:
    print("Test")
