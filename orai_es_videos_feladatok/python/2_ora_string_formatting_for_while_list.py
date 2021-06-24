"""
második óra
"""

# string formatting
age = 34
age_as_str = str(age)
print(f"you are " + age_as_str)  # kiírás stringként
print(f"you are {age}")  # kiírás integerként

## string formatting 2
name = "jose"
greeting = f"How are you, {name}?"
print(greeting)

# mi a probléma az f-stringgel?
name = "Jamal"
greeting = f"How are you, {name}?"
print(greeting)  # ha változtatod a name értékét, akkor nem frissül az újbóli felhasználásnál

### string formatting 3 (régi módszer, f-string előtt)
another_name = "Donnie"
another_name2 = "Darko"
final_greeting = "How are you, {} {}?"
donnie_greeting = final_greeting.format(another_name, another_name2)  #format funkcióval formázva f-string helyett
print(donnie_greeting)
# print(final_greeting.format(another_name, another_name2))
# donnie_greeting nélkül is kiprintelhető

#### ez a módszer vissza tud nyílni a final greeting sorra, ami korábban lett megadva
another_name = "Conor"
another_name2 = "Sarah"
connor_greeting = final_greeting.format(another_name, another_name2)
print(connor_greeting)

##### a két módszer keveréke
friend_name = "Brian"
final_greeting = "How are you, {name}"
brian_greeting = final_greeting.format(name=friend_name)
print(brian_greeting)

"""
IF STATEMENT
"""
friend = "Rolf"
user_input = input("Adj meg egy nevet: ")
if friend == user_input:
    print("Hello " + user_input + "!")
elif user_input == "Tom":  # elif == azonban, ha
    print("Hello Tom!")
elif user_input == "Loki":
    print("Hello Tom!")
else:
    print("That's your name")

# if, ha a feltétel nem egyenlő
sky_color = "blue"
user_input2 = input("Color: ")
if sky_color != user_input2:
    print("Cool")
elif sky_color == user_input2:  # red esetén ide már be sem jön... mert nem egyenlő a blue-val
    print("Red sky cool")
else:
    print("Cool cool")

age2 = 25
if 18 <= age <= 40:
    print("age 18-40")
elif 41 <= age <= 80:
    print("age 41-80")
else:
    print("age < 18 or age > 80")

"""
LIST
"""
car1 = "Tesla"
car2 = "Audi"
car2 = "BMW"

cars = ["Tesla", "Audi", "BMW"] # index 0, 1, 2
cars = ["Tesla", "Audi", "BMW"]
print(len(cars))  # lista hosszának lekérdezése
print(cars)  # lista elemeinek kiíratása
print(cars[0])  # lista adott indexű elemének lekérdezése
print(cars[1])
print(cars[2])

car_variable = cars[2]
print(car_variable)

vegyes_lista = ["Tesla", "Audi", "BMW", 2, 3, 2.2345]  ## a python engedi, de bad practice!!!

"""
FOR LOOP
"""

cars2 = ["Tesla", "Audi", "BMW", "Trabant"]
# iterációként a for loop bejárja és egyenként kiírja
for car in cars2:
    print(car)

# kiírásnál az upper()-rel csupa nagybetűsre alakítom
for car_upper in cars2:
    print(car_upper.upper())

# kiírásnál az lower()-rel csupa kisbetűsre alakítom
for car_lower in cars2:
    print(car_lower.lower())

# kiegészítve egy if-fel tovább tudjuk pontosítani a lekérdezéseket
for this_car in cars:
    if this_car == "Tesla":
        print("This car is Tesla")
    else:
        print("This car is a " + this_car)

number = [2, 3, 4, 5, 65, 78]
for num in number:
    print(num)

# létrehozunk egy számokat tartalmazó listát, aminek 10 eleme van: 0-tól 9-ig tart
numbers2 = range(10)
for i in numbers2:
    print(i)

# létrehozunk egy számokat tartalmazó listát, ami 1-től 19-ig tart
numbers3 = range(1, 20)  # az utolsó
for i in numbers3:
    print(i)

# # létrehozunk egy számokat tartalmazó listát, 1-től 20-ig, de kettesével ugrálva!!!
numbers4 = range(1, 21, 2)  # minden második számot kihagyja
for i in numbers4:
    print(i)

# NEM TANANYAG!!!
cars3 = ["Audi", "Trabant", "BMW", "Tesla", "Ford", "Ferrari"]
index = 0
for car in cars3:
    print(car, index)
    index += 1

# enumerate
for i, car in enumerate(cars3):
    print(car + " " + str(i))

# magic enumerate, a tuple-t ad vissza, amit listává kell alakítanunk
print(list(enumerate(cars)))


"""
WHILE CIKLUS
"""
number1 = 0
while number1 <= 10:
    print(number1)
    number1 += 1  # number = number + 1

# for ciklus break => az első találatkor álljon le (első találathoz szuper)
ok_or_not = ["ok", "ok", "ok", "ok", "faulty", "ok", "faulty"]
for status in ok_or_not:
    if status == "faulty":
        print(status)
        break
    print("ok or not status " + status)

# for ciklus continue => a találatot printelje és menjen tovább (több találathoz szuper)
for status in ok_or_not:
    if status == "faulty":
        print(status)
        continue  # continue visszaugrasztja a for ciklus elejére és nem hajta végre az utána levő részt
    print("ok or not status " + status)