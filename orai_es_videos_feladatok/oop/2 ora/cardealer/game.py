class Game:
    def __init__(self, dealership): # itt beadunk egy dealershipet hogy tudjunk vele doplgozni.
        self.dealership = dealership

    def print_menu(self):
        print("Welcome to PM car dealership!")
        print("Kocsi regisztralasa. Press number: Press number: 1")
        print("Osszes kocsi adatok lekerdezese. Press number: 2")
        print("Kocsi adatok lekerdezese. Press number: 3")
        print("Kocsi eladasa. Press number: 4")
        print("Kilepes az applicaciobol. Press number: 5")

    def ask_user_input_for_menu(self):
        user_input = input("What would you like to do?")
        return user_input

    def start_application(self):
        self.print_menu() # kinyomtatjuk a menut
        running = True
        while running:
            try:
                user_pick = int(self.ask_user_input_for_menu()) # bekerunk egy inputot, hogy mit akarun kcsinalni
                if user_pick == 1:
                    self.dealership.add_new_car() # A beadott dealership metodusait tudjuk meghivogatni
                elif user_pick == 2:
                    self.dealership.cars_details()
                elif user_pick == 3:
                    self.dealership.car_details_by_id()
                elif user_pick == 4:
                    self.dealership.car_sell()
                elif user_pick == 5:
                    running = False
                    print("Thank you. Have a nice day.")
                else:
                    print("Pick a number 1-5")
            except ValueError:
                print("Use numbers pls")