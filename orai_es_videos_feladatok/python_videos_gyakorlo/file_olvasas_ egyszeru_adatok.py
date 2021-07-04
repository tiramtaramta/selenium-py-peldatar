with open("file_egyszeru_adatok.txt", "r") as file:  # file a file változó neve
    obs = int(file.readline())  # integerként olvassuk be egy változóba a sort
    my_list = []  # készítünk egy üres listát
    for i in range(obs):
        my_list.append(int(file.read(1)))  # az egyes indexű sort hozzáadjuk a listához
        file.read(1)
print(my_list)


# kompakt megoldás
with open("file_egyszeru_adatok.txt", "r") as file:  # file a file változó neve
    obs = int(file.readline())  # integerként olvassuk be egy változóba a sort
    my_list = file.readline().split(" ")  # a stringet felvágjuk a separátor mentén
    print(my_list)  # figyelni kell, hogy itt stringként kapjuk vissza az elemeket

