# file elérések különböző rendszereken
# windows_file = "c:\\felhasznalok\\valaki"
# linux_file = "/home/valaki/"

# write-tal ha nem létezik, létrehozza
with open("file_iras_olvasas.txt", "w") as file:  # file a file változó neve
    file.write("alma")  # a változóra hívjuk meg a write függvényt

# appenddel, ha nem létezik, létrehozza. Ha létezik, hozzáfűzi
with open("file_iras_olvasas.txt", "a") as file:  # file a file változó neve
    file.write("alma")  # a változóra hívjuk meg a write függvényt

# read-del beolvassa
with open("file_iras_olvasas.txt", "r") as file2:  # file2 a file változó neve
    result = file2.read()  # a változóra hívjuk meg a read függvényt és az eredményt a result-ban tároljuk
print(result)



