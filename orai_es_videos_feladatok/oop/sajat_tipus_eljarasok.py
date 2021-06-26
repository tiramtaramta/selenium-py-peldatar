# __, _ mindig speciális függvényt jelent
# egy osztály alapján létrehozhatunk példányokak (jelen esetben a p változóban)
# erre a példányra meghívhatjuk az osztályban levő belső függvényeket, de külső függvényeket is.
# az osztály maga, alap esetben adatokat és viselkedéseket rendel a példányhoz

class Point:

    def __init__(self):
        self.x = 0  # attribútumok (belső változók, adatok)
        self.y = 0

    def print_p(self):  # belső függvény (viselkedés)
        print(self.x, self.y)

    def print_p2(self):
        self.print_p()


p = Point()  # létrehozunk a Point osztály alapján egy p változóban egy példányt
# print(p.x, p.y)
p.print_p2()  # a belső függvényt is meghívhatjuk, amely egy újabb belső függvényt hív meg


# áttekinthetőbb verzióban (újabb belső függvény meghívása nélkül):
class Point2:

    def __init__(self):
        self.x = 0
        self.y = 0

    def print_p(self):
        print(self.x, self.y)


q = Point2()
q.print_p()