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