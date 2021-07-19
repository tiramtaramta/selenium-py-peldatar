class Person:
    number_of_people = 0  # Class változó. Nem tartozik egyetlen objektumhoz sem. A classhoz tartozik.

    # csak a nevével készítjük el a konstruktort.
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # annotáció. a classhoz tartozó metódus
    def add_person(cls):
        cls.number_of_people = cls.number_of_people + 1  # ez hozzáad egyet, ha kreálunk egy persont

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people


p1 = Person("Jamal")
p2 = Person("Jill")
print(Person.get_number_of_people())  # classra hívjuk meg a metódust
