"""
első óra
"""""

# a változó bármi lehet
my_number = int()
my_number = 5
my_text = "text"

# számok fajtái
my_int = 5  # integer => egész szám (bármekkora egész szám lehet, de a 2-es verzióban korlátozva volt

# lekérdezhetjük a változó típusát
print(type(my_int))

my_float = 5.1  # float => lebegőpontos
print(type(my_float))

"""
Crl + D a sor végén => duplikálja a sort
Ctrl +Alt + lefelé nyil => lemozgatja
"""

number3 = 32.3e18  # scientific notation https://www.geeksforgeeks.org/display-scientific-notation-as-float-in-python/
number4 = .86j  # complex numbers https://www.tutorialspoint.com/complex-numbers-in-python

# stringek fajáti
string = str()
my_string = "car"
my_string2 = 'car'  # mindegy, melyiket használjuk, de legyen egységes a doksiban
print(type(my_string))

"""
Shift + F10 a program futtatása
Ctrl + Alt + l beigazítja a sorokat (hogy szépen mutasson)
Ctrl + / a kijelölt sorokat kikommenteli soronként
"""

# a bemenetet mindig be kell tenni egy változóba
user_input = input("Írj be nekem egy dolgot: ")
print(type(user_input))  # alapból mindig stringet olvas be!!!
print(user_input)

# első megoldás esetén a beolvasáskor alakítjuk integerré
user_number_input = input(int("Írj be nekem egy számot: "))
print(type(user_number_input))
adding = user_number_input + 5
print(adding)

# második megoldás esetén a műveletkor alakítjuk integerré
user_number_input2 = input("Írj be nekem egy számot: ")
print(type(user_number_input2))
adding = int(user_number_input2) + 5
print(adding)

# stringek összefűzése / egyik lehetséges verzió
first_name = "Krisztina"
last_name = "Connor"
full_name = first_name + " " + last_name
print(full_name)

# karakterlánc hosszának lekérdezése
print(len(first_name))
print(len(last_name))
print(len(full_name)) # a szóközt is beleszámolja

#beépített egyéb funkciók

# milyen karakterrel végződik? Ha igaz, akkor True értéket ad vissza
print(last_name.endswith("r"))

# milyen karakterrel kezdődik? Ha igaz, akkor True értéket ad vissza
print(last_name.startswith("r"))

# számok összefűzése
number1_to_add = 5
number2_to_add = 12

"""
Shift + F6 egyszerre átnevezi az összes változónevet, ha a sor elején állunk
"""

# összeadás
adding = number1_to_add + number2_to_add
print(adding)
# kivonás
sub = number2_to_add - number1_to_add
print(sub)
# osztás => mindig float numbert ad vissza!
div = number2_to_add / number1_to_add
print(div)
# szorzas
mult = number1_to_add * number2_to_add
print(mult)
# osztás egész számmal kiírva. Nem kerekítés!!! Csak levágja a végét
div2 = number2_to_add // number1_to_add
print(div2)
# a két szám osztásának maradéka (megvizsgáljuk, hogy egy szám páros-e, vagy páratlan)
# vagy azt, hogy maradék nélkül osztható-e
modulo = number2_to_add % number1_to_add
print(modulo)

#Boolean
#True / False
number6 = 10
print(number6 < 15)
print(number6 > 15)
print(number6 <= 10)

# össze lehet fűzni / halmozni
print(10 < number6 < 20) # csak akkor lesz True, ha mindkét feltétel igaz

# változóból szám beillesztése egy szövegbe
print("My number: " + str(number6))  # oldschool version
print(f"My number: {number6}")

"""
karaktersor, változó stb behelyezése valamibe
kijelölöm, és a bal felére beteszem a nyitó tag-et és ő automatikusan beteszi a végére
"""
