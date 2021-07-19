# Hozzunk letre egy Kutya osztalyt. Minden krealt kutyanak van neve,
# szine es egy szuletesi ideje.
# Legyen egy metodusa ami megmondja hogy milyen szinu az adott kutya.
# Legyen egy metodusa ami megmondja, hogy hany eves a kutya.
# (Csak az evet nezz, nem kell honapra pontosan).

import datetime


class Dog:

    def __init__(self, name, color, birthdate):
        self.name = name
        self.color = color
        self.birthdate = birthdate

    def get_color(self):
        return self.color

    def get_age(self):
        today = datetime.date.today()  # a mai nap lekérdezése
        age = today.year - self.birthdate.year  # elkérhető az év a dátumból (születési és az aktuális is)
        return age


name = input("Add meg a kutyád nevét: ")
color = input("Add meg a kutyád színét: ")
d1 = Dog(name, color, datetime.date(2013, 10, 23))  # konkrét dátum

print(d1.get_color())
print(d1.get_age())

