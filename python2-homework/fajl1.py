"""
Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!
"""
with open("adat.txt", "r") as file:
    print(file.readlines())
