class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def distance_from_zero(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5  # return, mert valamilyen eredményt ad vissza

    def __str__(self):
        return f"Point(x = {self.x}, y = {self.y})"
        # nem magában printel, hanem elkészíti az osztály string reprezentációját, melyet visszaad


p = Point(5, 12)  # az osztály tulajdonságaival létrehozunk egy példányt
# print(p)  # def __str__(self) nélkül ez így ezt fogja visszaadni: <__main__.Point object at 0x000001F33E134FD0>
q = Point(22, 14)
print(p, q)

