"""
írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat!
A kiírás több oszlopos legyen, és legfeljebb 10 soros.

A megoldashoz használd a beépített ord() es chr() függvényeket.
A megoldást egy charsandord.py nevű file-ban kell beadnod.
"""
# az 'a' karakterkódja 97
import cmd
x = 97
x_list = []

for i in range(26):
    i += x + 1
    # print(chr(int(i) - 1), ord(chr(int(i) - 1)))
    y = chr(int(i) - 1) + " " + str(ord(chr(int(i) - 1)))
    x_list.append(y)

cli = cmd.Cmd()
cli.columnize(x_list, displaywidth=22)
