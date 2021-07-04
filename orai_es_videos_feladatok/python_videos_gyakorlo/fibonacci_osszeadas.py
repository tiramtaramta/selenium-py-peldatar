# 0 + 1 + 1 + 2 + 3 + 5 ...

current = 1
previous = 0
my_sum = previous + current  # a két szám összege

while current < 4000000:
    if current % 2 == 0:  # ha páros a jelenlegi szám
        my_sum += current  # akkor adja hozzá az összeghez
    next = previous + current  # a következő szám legyen egyenlő az előző kettő összegével
    previous = current  # az előző szám legyen egyenlő a mostanival
    current = next  # a mostani legyen egyenlő a következővel

print(my_sum)  # kiprinteltetjük a páros számok összegét


################ fibonacci megoldása listával

fibonacci = [0, 1]
my_sum2 = 0
while fibonacci[-1] < 4000000:  # a tömb utolsó eleme, ami még kisebb, mint 4 millió
    if fibonacci[-1] % 2 == 0:  # ha páros a szám
        my_sum2 += fibonacci[-1]  # akkor hozzáadom az összeghez
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
    # if-en kívül minden egyéb esetben a fibonacci listához hozzá adom a két utolsó szám összegét

print(fibonacci, my_sum2)  # kiprinteltetjük a fibonacci számsor listáját és a benne található páros számok összegét
# ez a megoldás 2 alatt nem működik jól!