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

