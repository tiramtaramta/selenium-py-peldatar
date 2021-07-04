# readlines()-val beolvassa soronként
with open("file_iras_olvasas.txt", "r") as file:  # file a file változó neve
    result = file.readlines()  # ['kukacos alma\n', 'leves\n', 'valami\n', 'masik sor']
print(result)

# for ciklussal beolvassa soronként
with open("file_iras_olvasas.txt", "r") as file:  # file a file változó neve
    for line in file:
        print(line)

# readline()-nal beolvassa soronként
with open("file_iras_olvasas.txt", "r") as file:  # file a file változó neve
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())





