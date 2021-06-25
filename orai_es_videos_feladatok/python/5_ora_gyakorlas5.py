# Exercise 5:
new_dictionary5 = {"ONE": "AAA", "TWO": "BBB", "THREE": "CCC", "FOUR": "DDD", "FIVE": "EEE"}
# Replace the value associated with 'THREE' to '333'
# Replace the value associated with 'FOUR' to '444' only if it is currently mapped to 'DDD'

new_dictionary5.update({"THREE": 333})

if new_dictionary5["FOUR"] == "DDD":
    new_dictionary5.update({"FOUR": 444})

print(new_dictionary5)