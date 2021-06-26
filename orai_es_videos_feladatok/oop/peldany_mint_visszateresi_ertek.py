class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def distance_from_zero(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5  # return, mert valamilyen eredményt ad vissza

    def halfway(self, other_point):  # hol van féltávon egy pont a pont és egy másik pont között
        mx = (self.x + other_point.x) / 2
        my = (self.y + other_point.y) / 2
        return Point(mx, my)  # visszaadja a számítások alapján a két felezőpontot

    def __str__(self):
        return f"Point(x = {self.x}, y = {self.y})"
        # nem magában printel, hanem elkészíti az osztály string reprezentációját, melyet visszaad


p = Point(5, 12)  # az osztály tulajdonságaival létrehozunk egy példányt
q = Point(22, 14)
print(p.halfway(q))

print("________________________")

# ha szorosan hozzátartozik az osztályhoz a függvény, akkor bele szoktuk írni
# ha nem, akkor megírhatjuk úgy is, hogy a halfway függvény külső függvényként van megírva:


def halfway2(one_point, other_point):  # hol van féltávon egy pont a pont és egy másik pont között
    mx = (one_point.x + other_point.x) / 2
    my = (one_point.y + other_point.y) / 2
    return Point(mx, my)  # visszaadja a számítások alapján a két felezőpontot


class Point2:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def distance_from_zero(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5  # return, mert valamilyen eredményt ad vissza

    def __str__(self):
        return f"Point(x = {self.x}, y = {self.y})"
        # nem magában printel, hanem elkészíti az osztály string reprezentációját, melyet visszaad


r = Point2(5, 12)  # az osztály tulajdonságaival létrehozunk egy példányt
s = Point2(22, 14)
print(halfway2(r, s))

