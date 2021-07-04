with open("file_iras_olvasas.txt", "r") as file:  # file a file változó neve
    result = file.read(10)  # meg tudjuk adni, hogy hanyadik karakterig olvassa be (enter és space is számít!)
    result2 = file.read(2)
print(result)
print(result2)
