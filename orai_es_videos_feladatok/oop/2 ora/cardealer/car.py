class Car:
    def __init__(self, brand, age, color):
        self.brand = brand
        self.age = age
        self.color = color

    def __str__(self):
        return f"Brand: {self.brand}, age: {self.age}, color: {self.color}"