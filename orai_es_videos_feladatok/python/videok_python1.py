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




