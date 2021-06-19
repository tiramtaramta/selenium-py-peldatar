"""
Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
"""
with open("adat.txt", "r") as file:
    adat_list = file.readlines()
    print(* [s[:-1] for s in adat_list], sep = " ")
