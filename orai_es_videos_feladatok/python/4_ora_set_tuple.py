############ SET
# Mi a set? Olyan, mint a lista, de ebben nem lehet egyforma elem;
# duplikált elemeket úgy lehet egyszerűen törölni a listából, ha set-et másolok belőle
# bekerül, de a printben már nem lesz ott

# a set elemeit nem lehet módosítani, de lehet törölni és hozzáadni

# Ez egy lista
number_list = [1, 1, 2]

# Ez egy set
number_set = {1, 1, 2}

print(number_list)
print(number_set)

# Új elem hozzáadása a set-hez.
number_set.add(2)  # add és nem append
print(number_set)

# Elem törlése a set-ből.
number_set.remove(2)  # nem index, hanem érték alapján!
print(number_set)

# A set printnél nem tartja meg a sorrendet, hanem összekeverve printeli ki
letter_set = {'A', 'a', 'B', 'b', 'C', 'c'}
print(letter_set)

letter_list = ['A', 'a', 'A', 'B', 'b', 'C', 'C', 'c']
print(set(letter_list))  # a duplikált lista setként printelve, kidobálja a dupla elemeket
# két lista összehasonlítására is tökéletesen alkalmas (szűrésre is használható a set)


################ Tuple
# A Tuple olyan, mint a lista, de nem módosítható a tartalma!!!
numbers = (21, -5, 6, 9)
print(numbers)
print(numbers[1])
print(numbers[0:3])  # a 3.index már nincs benne (excluded)
print("________")

# for ciklussal bejárható
for i in numbers:
    print(i)

languages = ("Python", "Java", "JavaScript", "C#")
# languages[0] = "Ruby" Ez errort fog adni, mert az elemeke nem módosíthatók.
print(languages)

# ha mégis hozzá szeretnénk adni, akkor listává alakítjuk, hozzáadjuk és végül tuple-t készítünk belőle
convert_to_list = list(languages)
convert_to_list.append("Ruby")
print(convert_to_list)
convert_back = tuple(convert_to_list)
print(convert_back)

# 2 Tuple-t össze lehet fűzni úgy, hogy egy új memóriacímre helyezi
friends = ("Rolf", "Bob", "Anne")
friends2 = friends + ("Jen", "John")
friends3 = friends + friends2
print(friends2)
print(friends3)