# Exercise 1
# We give you a list with numbers. Write out the list elements to a number.txt file
# line by line!
import csv

my_number = [5, 12, 16, 19, 21, 13]

# with open('number.txt', 'a') as file:
#     for number in my_number:
#         file.write(str(number) + "\n")
# with open('number.txt', 'r') as file:
#     result = file.read()
#     print(result)


# Exercise 2
# Write an application which is going to count how many element are identical in the second list like in the
# first list. This is NOT case sensitive.
# num1 = [2,3,4,5]
# num2 = [2,4,5,6,7,8,9,2]
# Result = 4
# my_list1 = ["Tom", "Christine", "Mark", "Daniel"]
# my_list2 = ["tom", "Tom", "Beatrix", "Job", "Frodo", "Daniel", "daniel", "Gandalf", "mark"]
# x = 0
# for i in my_list1:
#     for j in my_list2:
#         if i.lower() == j.lower():
#             x += 1
# print(x)


# Exercise 3
# You have to create a csv file (under name: petofi), with this text:
# Gondűző, borocska, mellett
# Vígan, illan, életem,
# Gondűző, borocska, mellett,
# Sors, hatalmad, nevetem,
# És, mit, ámultok, ha mondom,
# Hogy, csak, a, bor, istene,
# Akit, én, imádok, aki,
# E, kebelnek, mindene,
# Write out every row every second word to the another file (file name should be: res.csv). You have to skip the first line!

with open('petofi.csv', 'w', encoding="UTF-8") as pet:
    pet.write(
        "Gondűző, borocska, mellett \nVígan, illan, életem,\nGondűző, borocska, mellett,\nSors, hatalmad, nevetem,\nÉs, mit, ámultok, ha mondom, \nHogy, csak, a, bor, istene, \nAkit, én, imádok, aki,\nE, kebelnek, mindene")
    pet.close()

with open('petofi.csv', 'r', encoding="UTF-8") as p_file:
    with open('res.csv', 'w', encoding="UTF-8") as res_file:
        next(p_file)
        file_table = csv.reader(p_file, delimiter=',')
        for row in file_table:
            res_file.write(row[1])
            res_file.write("\n")