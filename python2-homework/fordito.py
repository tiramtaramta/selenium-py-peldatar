"""
Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre
a lista elemeit fordított sorrendben!
"""
user_list = []
while True:
    user_input = int(input("kérlek adj meg egy pozitív egész számot: "))
    user_list.append(user_input)
    if user_input == 0:
        user_list.reverse()
        print(user_list)
        break

# solution 2

# flag = True
# numbers = []
#
# while flag:
#     try:
#         user_input = input("your number: ")
#         if int(user_input) < 0:
#             print("Number can not be negative")
#         elif int(user_input) == 0:
#             flag == False
#         else:
#             numbers.append(int(user_input))
#     except:
#         print("input must be a number")
# numbers.reserve()
# print(numbers)