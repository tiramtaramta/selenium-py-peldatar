# Create a txt file in the same folder where you store this .py module. ( name the txt file:   data)
# The text in this data.txt:
# Tom Denem alias
# Voldemort

import csv

#######  FILE READING OLD SCHOOL VERSION!  #####################

my_txt = open('data.txt', 'r')  # Nyissuk meg a file-t olvasásra.
txt_content = my_txt.read()  # read() funkcióval beolvassul. Az egész file-t: 'Tom Denem alias\nVoldemort'
# txt_content = my_txt.read(6)  # ez csak az első hat karaktert olvassa be
my_txt.close()  # limitált, hogy hány file lehet nyitva, így bezárjuk, ha már nincs rá szükség.
print(txt_content)


#######   OPEN FILE AND READ WITH OPEN:
with open('data.txt', 'r') as file:  # adunk neki egy alias nevet (ninckname).
    res = file.read()
    print(res)
    # file.close()  # a with open megnyitásnál nem kell bezárni a file-t, mert bezárja magától



########  FILE WRITING!  ############################

# Jó gyakorlat, ha a file megnyitása előtt kérünk be inputot.
# Így nem nyitjuk meg feleslegesen a file-t.
user_input = input("What is your name?")

with open('data.txt', 'w') as file:  # Nyissuk meg írásra. A w felülírja a benne levő tartalmat
    result = file.read(user_input)
    print(result)

# Ellenőrizzük, hogy mi van a data.txt-ben! (Felülírta az összes adatot, a megadott névvel)
with open('data.txt', 'r') as file:
    result = file.read()
    print(result)



# ######## FILE OPEN FOR APPEND ############
with open('data.txt', 'a') as file:
    file.write("Kutya ")
    file.write("Cica ")
    file.write("\n")
    file.write("Cica")
with open('data.txt', 'r') as file:
    result = file.read()
    print(result)



########  FILE ERROR HANDLING ##################
try:
    with open('../data.txt', 'r') as file:  # elérési útnak a felette levő mappában fogja keresni, így elszáll
        txt_content = file.read()
        print(txt_content)
except FileNotFoundError:
    print("I could not find any file under this name")
except:
    print("Barmit elkapok")  # ezt érdemes belerakni, hogy ne csak a filenotfound hiba jelenjen meg



####### FILE READING LINE BY LINE
# Olvassuk be soronként a file tartalmát readline()
with open('data.txt', 'r') as file:
    txt_content = file.readline()
    print(txt_content)


# Sorok beolvasása READLINE WHILE CIKLUSSAL
with open('data.txt', 'r') as file:
    txt_content = file.readline()
    while txt_content:
        print(txt_content, end='')  # azért kell ide az end= '', hogy ne legyenek printnél üres sorok (automatikusan end='\n')
        txt_content = file.readline()


# # Sorok beolvasása FOR CIKLUSSAL:
with open('data.txt', 'r') as file:
    for line in file:
        print(line, end="")


# # Sorok beolvasása READLINES ciklusok nélkül ==> listába    readlines().
my_txt = open('data.txt', 'r')
txt_content = my_txt.readlines()
print(txt_content)
my_txt.close()

# Sorok beolvasása READLINES ciklusok nélkül ==> listába    readlines().
with open('data.txt', 'r') as file:
    txt_content = file.readlines()
    print(type(txt_content))
    print(txt_content)



############### CSV file - Comma-Separated Values  ##############    reader()
with open('movies.csv', 'r', encoding="utf-8") as csv_file:  # encoding if you use special characters like: á,é
    table_reader = csv.reader(csv_file)  # csv.reader paranccsal beolvassuk egy table_reader vátozóba
    for row in table_reader:  # majd for ciklussal soronként kiprinteljük. Minden sor egy lista!!!
        print(row)

# Beolvassuk a file-t, de csak a title értékeket printeljük ki
with open('movies2.csv', 'r', encoding="utf-8") as csv_file2:
    table_reader = csv.reader(csv_file2, delimiter=';')  # delimeterrel mondjuk meg, hogy milyen elválasztók vannak a file-ban
    for row in table_reader:
        print(row[0])  # nulladik indexű elemet printeljük ki



#######  Egymásba ágyazott for ciklusok
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

for i in num1:
    for k in num2:  # addig fogja az első ciklus az első elemet, amíg a második ciklus végig nem ment!!! utána vált
        print(f"I am loop1: {i}, i am loop 2: {k}")


# Ha a k osztva i-vel 0 eredményt ad (k % i == 0) az if ágban, akkor printeli ki az i és a k értékét
for i in num1:
    for k in num2:
        if k % i == 0:
            print(f"i value: {i} : k value: {k}")