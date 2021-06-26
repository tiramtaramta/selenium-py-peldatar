# x = 0
# y = 0
# points_list = [(1, 2), (1, 23)]

# ezek helyett osztályokat hozhatunk létre. Az osztályok neve mindig nagybetűvel kezdődik.
# az osztályok tartalmazhatnak saját függvényeket is (vannak előre beépített függvények is hozzájuk)

class Point:

    def __init__(self):  # inicializáló függvény, amely még csak egy minta, melyet később meg kell hívni
        self.x = 0
        self.y = 0


p = Point()  # készítettünk egy saját típust, ami meghívja az osztályt
p.x = 12  # az értékeket is megadhatjuk
p.y = 24
q = Point()

print(p.x, p.y, q.x, q.y)