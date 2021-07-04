# megszámoljuk, hogy egy camelCase szóban hány szótag szerepel

def camel_case_counter(input_str):  # stringet adunk be neki
    my_count = 1  # egy szótag mindenképpen lesz. akkor is, ha nincs benne camelCase
    for character in input_str:
        if character.isupper():  # ha a karakter nagybetű
            my_count += 1
    return my_count  # a szám lesz a visszatérő érték


camel_case = "myHouseIsOnFire"
result = camel_case_counter(camel_case)  # elmentjük egy változóban a kapott számot
print(f"A '{camel_case}' szó {result} szótagot tartalmaz")
