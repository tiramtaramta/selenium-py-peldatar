# superclass (felül levő általános class)
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print("I dont know what i say")


# specializált classt így is létre lehet hozni (az inicializálás felülírásával
class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)  # így lehet áthívni a superclass konstruktorát
        self.color = color  # és kiegészíteni az egyedi elemekkel

    def speak(self):
        print("Meow")

    def show(self):
        print(f"i am {self.name} and I am {self.age} years old and i am {self.color}")


# lehet úgy is, hogy simán örökölje a superclassból és semmit nem konkretizálunk
class Dog(Pet):

    def speak(self):  # felülírtuk a fenti speak metódust
        print("Bark")


# mindent örököl a superclassból
class Fish(Pet):
    pass


p = Pet("Tim", 6)
p.show()
p.speak()

c = Cat("Bill", 8, "black")
c.show()
c.speak()
c1 = Cat("Jill", 1, "white")
c1.show()
c1.speak()
#
d = Dog("Jamal", 5)
d.show()
d.speak()
#
f = Fish("Booble", 2)
f.speak()
