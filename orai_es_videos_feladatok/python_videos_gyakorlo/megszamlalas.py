# MEGSZÁMLÁLÁS
# az adott tulajdonsáú elemek megszámlálása egy sorozatban

my_list = [2, 1, 5, 5, 3, 2, 1, 1]

my_count = 0
for element in my_list:
    if element == 1:  # ha az elem 1, akkor a my count számát növeljük
        my_count += 1
print(my_count)