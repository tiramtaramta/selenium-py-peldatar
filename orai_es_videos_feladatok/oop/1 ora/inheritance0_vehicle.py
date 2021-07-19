# öröklődés (egy általános classból specifikálunk egy másik classt)
class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def brum_brum(self):
        print("brum brum")


# ez a class mindent megörököl a vehicle-től
class Bus(Vehicle):
    pass


# ez a class mindent megörököl a vehicle-től
class Car(Vehicle):
    pass


# így lehet létrehozni a speciálisabb
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

School_bus.brum_brum()  # a vehicle konstruktorában szerepel csak, de a gyerekre is meghívható
