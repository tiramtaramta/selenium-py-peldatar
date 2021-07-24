from car import Car


class Dealership:
    def __init__(self):
        self.carList = []  # létrehozáskor üres listát kap

    def add_new_car(self):  # Bekérjük az adatokat
        brand = input("Brand? :")
        age = input("Age? :")
        color = input("Color? :")
        new_car = Car(brand, age, color)  # egy változóban létrehozzuk a Car alapján az autót
        self.carList.append(new_car)  # majd hozzáadjuk a listához

    def cars_details(self):
        for car in self.carList:  # for ciklussal bejárjuk a Dealership autóit
            print(car.brand, car.age, car.color)  # majd printeljük
            # print(car) # A __str__ miatt igy is lehetne

    def car_details_by_id(self):
        try:
            car_index = int(input("Which car you wanna check?: "))  # bekérünk egy id-t
            print(self.carList[car_index])  # id alapján megkeressük az autót
        except IndexError:
            print("Given number is out of index")  # ha olyan számot ad meg, ami nem létezik
        except:
            print("Use numbers")  # ha nem számot ad meg

    def car_sell(self):
        try:
            car_index = int(input("Which car you wanna sell?: "))  # bekérünk egy id-t
            del self.carList[car_index]  # töröljük a listáról
            for car in self.carList:
                print(car)  # majd kiprinteltetjük a maradékot
        except IndexError:
            print("Given number is out of index")  # ha olyan számot ad meg, ami nem létezik
