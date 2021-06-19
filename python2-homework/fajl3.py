"""
Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
"""
with open("adat.txt", "r") as file:
    adat_list = file.readlines()
    adat_string = [s[:-1] for s in adat_list]
    file.close()

with open("adat2.txt", "w") as file:
    for element in adat_string:
        file.write(element + " ")
    file.close()
