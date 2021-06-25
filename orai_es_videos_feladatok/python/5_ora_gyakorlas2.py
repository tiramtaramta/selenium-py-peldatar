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