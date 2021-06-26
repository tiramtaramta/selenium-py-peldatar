# az __init__ egy különleges metódus a pythonban.
# Ha szeretném, hogy saját értékei, legyenek akkor az init függvénybe kell beleírni

class Point:
    def __init__(self, _x, _y):  # itt megadhatjuk neki, hogy ne konkrét értéke legyen
        self.x = _x
        self.y = _y


p = Point(5, 12)  # példányosításnál már megadhatom az init paramétereke
print(p.x, p.y)

# q = Point()  # így már nem tudunk létrehozni példányt, mert értéket kell neki adni (hibára fog futni)
# print(q.x, q.y)


class Point2:
    def __init__(self, _x=0, _y=0):  # itt megadhatjuk neki, hogy legyen egy alapértelmezett értéke is
        self.x = _x
        self.y = _y


r = Point2(10, 21)  # példányosításnál megadhatom az init paramétereket
print(r.x, r.y)

s = Point2()  # ha viszont nem adom meg, akkor az alapértelmezett 0 lesz mellé rendelve
print(s.x, s.y)