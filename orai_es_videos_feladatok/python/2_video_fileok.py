############### filekezelés pythonból #########
# minden rendszeren más
# win
# ws_file = "c:\\Felhasznalok\\ valaki"  # azért kell a dupla, mert a sima \ az kilépő karakter
# unix_file = "/home/valaki  # itt nincs gond


####### file olvasas és írás ##############

with open("input.txt", "w") as file:  # az input.tx file-ba szeretnék írni (f a file rövidítése)
    file.write("alma")

with open("input.txt", "r") as file: # file olvasása az input.txt-ből
    result = file.read()
    print(result)

with open("input.txt", "a") as file:  # az a-val hozzáfűz (ha nem létezik, létrehozza)
    file.write("alma")

### hibák írás és olvasás során
# no such file or directory: "input.txt"
# TILOS OLVASTATNI ÉS ÍRNI EGYSZERRE

### file hozzáfűzés és írás kapcsolata
# w  ==> ami van benne azt törli
# a ==> ami van benne ahhoz hozzáfűzi

############ file soronkénti olvasása

### soronként tölti be egy listába
with open("input.txt", "r") as f:
    result = f.readlines()
print(result)

### így soronként tudom beolvastatni
with open("input.txt", "r") as f:
    result = f.readline()
    result = f.readline()
print(result)

### for ciklussal soronkénti beolvasás
#pl.:
with open("input.txt", "r") as f:
    for line in f:
        print(line)

### fájlok beolvasása karakterenként
with open("input.txt", "r") as f:
    result = f.read(2)  # megadható, hogy hány karaktert olvasson be
    result2 = f.read(5)  # megadható, hogy hány további karaktert olvasson be
print(result)
print(result2)

### file-ból egyszerű adatok olvasása
# érdemes kifejezetten a file-ra készíteni a programot
with open("input.txt", "r") as f:
    obs = int(f.readline())
    my_list = f.readline().split(" ")  # ez egy listát ad vissza, ami a szeparátor mentén szétvágja a szöveget
    print(my_list)
    # my_list = []
    # for i in range(obs):
    #     my_list.append(int(f.readline(1)))
    #     f.read(1)
    # print(my_list)



