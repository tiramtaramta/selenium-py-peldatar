"""
 * Hozz létre egy Person superclass-t és egy Student subclass-t.
 * A Person-nak az alábbi attribútumai vannak:
 *  - name (String)
 *  - age (int)
 *  - gender (String, M/F)
 *  Használj toString metódust az összes class-ra.
 *
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} and i am {self.gender}"