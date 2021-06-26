def print_point(pt):  # a pt lesz, amit át akarunk adni
    print(f' x = {pt.x}, y = {pt.y}')


class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def distance_from_zero(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5  # return, mert valamilyen eredményt ad vissza


p = Point(5, 12)  # az osztály tulajdonságaival létrehozunk egy példányt
print_point(p)  # saját osztályból létrehozott példányt lehet használni külső függvényekben is
