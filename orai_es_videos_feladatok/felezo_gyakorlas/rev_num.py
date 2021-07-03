user_number1 = int(input("Kérlek add meg az első számot: "))
user_number2 = int(input("Kérlek add meg a második számot: "))


def between(a, b):
    numbers = []
    a = user_number1
    for a in range(a, b + 1):
        numbers.append(a)
        a += 1
    print(numbers)


between(user_number1, user_number2)


# Kocka megoldasa
# def between(a, b):
#     numbers = []
#     a = user_number1
#     for a in range(a, b + 1):
#         numbers.append(a)
#     return numbers
#
#
# print(between(user_number1, user_number2))

