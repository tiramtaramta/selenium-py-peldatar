"""
írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat!
A kiírás több oszlopos legyen, és legfeljebb 10 soros.

A megoldashoz használd a beépített ord() es chr() függvényeket.
A megoldást egy charsandord.py nevű file-ban kell beadnod.
"""
# az 'a' karakterkódja 97
x = 97
y = 65
for i in range(26):
    i += x + 1
    print(chr(int(i) - 1), ord(chr(int(i) - 1)))
