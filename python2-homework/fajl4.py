"""
Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba!
"""
with open("adat.txt", "r") as file:
    adat_list = file.readlines()
    file.close()

with open("adat3.txt", "w") as file:
    for element in adat_list:
        file.write(element)
    file.close()
