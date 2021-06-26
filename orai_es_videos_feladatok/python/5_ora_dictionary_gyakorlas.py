# Exercise 1:
# Add the key-value pair 'ONE-111' only if it is not present in map
# Add the key-value pair 'FIVE-5' only if it is not present in map
# Print the key-value pairs of map
new_dictionary = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4}

for i in new_dictionary:
    if i == "ONE":
        break
    else:
        new_dictionary["ONE"] = 111

print(new_dictionary)

new_dictionary["FIVE"] = 5
print(new_dictionary)

for key, value in new_dictionary.items():
    print(key, value)


#############################################
# Exercise 2:
new_dictionary2 = dict()
new_dictionary2[111] = 111.111
new_dictionary2[222] = 222.222
new_dictionary2[333] = 333.333
new_dictionary2[444] = 444.444
new_dictionary2[555] = 555.555
# Print the number of key-value pairs
# Clear the map
# Check the number of key-value pairs after clearing the map

x = 0
for i in new_dictionary2:
    x = x + 1
print(f"{x} db elem van benne")

new_dictionary2.clear()

y = 0
for i in new_dictionary2:
    y = y + 1
print(f"{y} db elem van benne clear után")


#############################################
# Exercise 3:
new_dictionary3 = {1: "AAA", 2: "BBB", 3: "CCC", 4: "DDD", 5: "EEE"}
# Retrieve the keys from the map and print it
# Retrieve the values present in the map and print them

for i in new_dictionary3.keys():
    print(i)

for i in new_dictionary3.values():
    print(i)


#############################################
# Exercise 4:
new_dictionary4 = dict()
new_dictionary4["ONE"] = "AAA"
new_dictionary4["TWO"] = "BBB"
new_dictionary4["THREE"] = "CCC"
new_dictionary4["FOUR"] = "DDD"
new_dictionary4["FIVE"] = "EEE"
# Print the key-value pairs of the map
# Remove the mapping for the key 'ONE'
# Remove the mapping for the key 'THREE' only if it is currently mapped to 'DDD'
# Remove the mapping for the key 'FIVE' only if it is currently mapped to 'EEE'
# Print the key-value pairs of the map

for key, value in new_dictionary4.items():
    print(key, value)

del new_dictionary4["ONE"]

if new_dictionary4["THREE"] == "DDD":
    del new_dictionary4["THREE"]

if new_dictionary4["FIVE"] == "EEE":
    del new_dictionary4["FIVE"]

for key, value in new_dictionary4.items():
    print(key, value)


#############################################
# Exercise 5:
new_dictionary5 = {"ONE": "AAA", "TWO": "BBB", "THREE": "CCC", "FOUR": "DDD", "FIVE": "EEE"}
# Replace the value associated with 'THREE' to '333'
# Replace the value associated with 'FOUR' to '444' only if it is currently mapped to 'DDD'

new_dictionary5.update({"THREE": 333})

if new_dictionary5["FOUR"] == "DDD":
    new_dictionary5.update({"FOUR": 444})

print(new_dictionary5)


#############################################
# Exercise 6:
# Exercise: You will get list which contains a few dictionaries with a student name and a grade. Print out each of
# them nicely formatted sentence. "Name has a grade of X."
students = [
    {"name": "Jamal", "grade": 90},
    {"name": "Jay", "grade": 75},
    {"name": "Bob", "grade": 55},
    {"name": "Anne", "grade": 95}
]

for i in students:
    name = i["name"]
    grade = i["grade"]
    print(f"{name} has a grade of {grade}")