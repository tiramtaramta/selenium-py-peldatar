"""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
Ezen a néven fogadható el a megoldás.

Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
Írja ki ezek után a beolvasott számok összegét!
A megoldást egy tenbelow.py nevű file-ban kell beadnod.
"""

x = 0
while True:
    my_x = int(input())
    if my_x < 10:
        x += my_x
    else:
        break
print(x)
