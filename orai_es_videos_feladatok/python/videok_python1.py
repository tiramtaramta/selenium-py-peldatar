hello_world = "Hello World"
print(hello_world)

# primitív adattípusok
print("A")  # str
print(12)  # int
print(0.5)  # float
print(True, False)  # bool

# változók nevezéktanja
alma = 12
alma2 = 12
class_alma = 12
_alma = 12  # speciális jelentésű változónév (ne használjuk, csak ha szándékos)

# kifejezések nemcsak sorról sorra írhatók, hanem halmozhatók is
alma = 12
print(alma)
alma = "Hello"
print(alma)

print(3 + 5 + 8 / 2)
print(alma * 3)

# operátorok
print(1 + 2, 1 - 1, 2 * 3, 60 / 20, (1 + 3) * 2)
print(alma * 3)  # almaalmaalma
print(60 // 20, 60 / 20)  # 3, 3.0  // egész osztás / egész osztás tizedesjegy
print(5 % 3)  # modulo (mennyi marad osztás után)
print(2 ** 4)  # hatványozás 2*2*2*2

# operátor precedencia
# docs.python.org/3/reference/expressions.html

# típusok közti váltás
alma = "Hello"  # str
print(type(alma))  # lekérdezhető a változó típusa
print(type(True))  # bool
alma = 3.3
print(type(alma))  # float
print(int(alma) / 2)  # 1.5
alma = "3.3"
print(float(alma) + 2)  # 5.3

# karakterláncok műveletei
print("hello" + " world")  # két string összeadható (concate)
print("hello" * 3)  # hellohellohello

# felhasználói bemenet kezelése
input()
input("Kérlek adj meg egy számot: ")
age = input("Hány éves vagy? ")  # alapból az input mindig stringet ad be
print(age)
age = int(input("Hány éves vagy? "))
print(age - 1)

# vezérlési szerkezetek
# for ciklus (számláló ciklus)
for i in range(5):
    print(i)  # 0 1 2 3 (az 5. index már nem tartozik bele!!! excluded

my_list = [0, 1, 2, 3, 4]
for i in my_list:
    print(i)

for i in [0, 1, 2, 3, 4]:
    print(i)

# for ciklus elemenként
my_list = [0, 1, 'alma', 3, 4]
for i in my_list:
    print(i)  # az i felveszi a lista elemeinek értékét

x = 0
for i in range(3):  # nem fontos a ciklusváltozót a cikluson belül használni
    my_input = input()
    x += int(my_input)
print(x)

# boole algebra
my_ture = True
my_false = False
print(my_ture, my_false)

print(3 == 5)  # False
print(3 == 5 - 2)  # True

# logikai operátorok
alma = 5
korte = 6
print(alma == 5)  # az alma egyenlő-e 5-tel  True
print(alma != 5)  # igaz-e, hogy az alma nem egyenlő 5-tel  False
print(3 < 5, 3 > 5, 3 <= 5, 3 >= 5, 5 <= 5)  # True False True False True
print(alma <= korte)

# logikai és vagy kapcsolatok
print(5 == 5 and 3 < 4)  # igaz és igaz => True
print(5 == 5 and 3 > 4 and True)  # igaz és hamis és igaz => False

print(5 == 5 or 3 < 4)  # igaz és igaz => True
print(5 == 5 or 3 > 4)  # igaz és hamis => True
print(5 > 5 or 3 > 4)  # hamis és hamis => False
print(5 == 5 and (3 < 4 or 5 > 6))  # True

# eldöntés logikai művelet
my_input = input("Adj meg egy számot: ")
if int(my_input) > 5:
    print("This is true")
elif int(my_input) >= 3:
    print("This is second true")
else:
    print("This is false")

# eldöntés több feltétellel
x = int(input("Adj meg egy számot"))
if x < 10 and x % 2 == 0:
    print("ok")
elif x % 2 != 0:
    print("Not ok")
else:
    print("number")

# eldöntések egymásba ágyazása
x = int(input("Adj meg egy számot"))
if x > 5:
    print("ok")
    if x < 10:
        print("small")
    else:
        print("big")
else:
    print("not ok")

# while ciklus (elöl tesztelős ciklus) Amíg a feltétel igaz, addig ismétli a ciklust
x = int(input("Adj meg egy számot"))
while x < 5:
    print("hello")  # ha kisebb, mint 5
    x += 1  # enélkül végtelen ciklus lenne

# ciklusok vezérlése (Break, Continue)
for i in range(5):
    print(i)  # felveszi a 0 értéket
    break  # majd leáll
print("done")

for i in range(5):
    if i == 3:
        break
    print(i)
print("done")


my_x = 10
while my_x > 0:  # addig fut, amíg nagyobb nullánál
    print(my_x)
    if my_x == 5:  # ha 5, akkor leáll
        break
    my_x -= 1

while True:  # addig fut, amíg be nem adjuk az 5-öt
    my_x = int(input())
    if my_x == 5:  # ha 5 akkor leáll
        break

for i in range(5):
    if 3 == i:  # ha i = 3-mal, akkor azt nem nyomtatja ki
        continue
    print(i)


# függvények
def fuggveny(val_to_print):  # ami paraméterként bejön, azt fogjuk kinyomtatni
    print("hello")
    print(val_to_print)


for i in range(5):
    fuggveny(i)


# függvény paraméterek
def addition(in_var, in_var_other):
    return in_var + in_var_other  # a return fontos, hogy vissza is térjen valami érték


x = addition(3, 5)
print(x)
my_x = 1
my_y = 12
y = addition((my_x, my_y))
print(y)


# függvény törzs
def addition(in_var, in_var_other, alma):
    return (in_var + in_var_other) * alma  # a return fontos, hogy vissza is térjen valami érték


my_alma = 12
my_x = 1
my_y = 12
y = addition(my_x, my_y, my_alma)
print(y)






