# A Class egy váz -> Objektumokat hozunk létre a váz alapján.

# létrehozunk egy person osztályt (modellt)
class Person:
    # az inicializáló metódusban (konstruktor) mondjuk meg,
    # hogy mi alapján kell létrehozni egy objektumot (név, kor, hajszín)
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color

    # definiálunk egy walk nevű metódust
    def walk(self):
        print(self.name + ' is walking...')

    # definiálunk egy speak nevű metódust
    def speak(self):
        print('Hello my name is ' + self.name + ', and i am ' + str(self.age) + ' years old')

    # toString metódus fontos!!! print(john)-hoz mindenképpen kell, különben memóriacímet kapunk
    def __str__(self):
        return "Name: {0}, and age: {1}".format(self.name, self.age)  # 0. és 1. elem a name és az age
        # return f"Name: {self.name} and age: {self.age}"


# itt hozzuk létre a person-t egy john nevű változóban
john = Person('John', 22, "black")
print(john)  # kiprinteljük john tulajdonságait

# john walk metódusát meghívjuk
john.walk()  # self -> rejtett attribútum, ami önmagára hivatkozik, ezért nem kell beírni
john.speak()

tom = Person('Tom', 18, "red")
print(tom)

# tom walk metódusát meghívjuk
tom.walk()
tom.speak()

print(john.name + " " + str(john.age))
