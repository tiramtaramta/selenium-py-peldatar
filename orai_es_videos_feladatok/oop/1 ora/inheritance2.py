# superclass
class Bird:

    def __init__(self):
        print("Bird is ready")  # létrehozáskor írja ki, hogy készen van (ez mindig lefut!)

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# bizonyos dolgokat lehet fentről örökölni, felülírni és újakat hozzáadni.
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")  # pingvin kész

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
