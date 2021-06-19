"""
Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!
"""
with open('adat.txt', 'r') as in_file, \
     open('adat4.txt', 'w') as out_file:

    for element in in_file.readlines():
        out_file.write(element)

in_file.close()
out_file.close()
