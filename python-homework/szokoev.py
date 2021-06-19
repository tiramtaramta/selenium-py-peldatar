"""
Szökőév?
Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e.
Szökőév minden negyedik,
nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.)
A függvény visszatérési értéke legyen logikai típusú!
Tipp( % maradekos osztas operátor)
Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
Használd az előbb megírt függvényt!
Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.
A megoldást egy szokoev.py nevű file-ban kell beadnod."""


def szokoev(a):
    if a % 4 == 0 and a % 400 == 0:
        return True
    elif a % 4 == 0 and a % 100 == 0 and a % 400 != 0:
        return False
    elif a % 4 == 0:
        return True
    else:
        return False


for i in range(5):
    if szokoev(int(input("Kérlek adj meg egy évszámot: "))):
        print("Szökőév.")
    else:
        print("Nem szökőév.")
