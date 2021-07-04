# SOROZATSZÁMÍTÁS

# egy sorozat elemein vegiglepkedve hajtsunk vegre egy muveletet
def my_function(_current_element, _element):
    pass


my_list = [2, 3, 4, 7, 8, 1]
current_element = my_list[0]  # a lista első eleme lesz a current element

for i in range(1, len(my_list)):
    current_element = my_function(current_element, my_list[i])
print(current_element)

# sorozatszamitas specialis eset pl: az összegzes
# adjuk ossze egy sorozat elemeit


def add_elements(_my_sum, _element):
    return _my_sum + _element


my_list2 = [2, 3, 4, 7, 8, 1]
my_sum = my_list[0]

for i in range(1, len(my_list2)):
    my_sum = add_elements(my_sum, my_list2[i])
print(my_sum)

# egyszerűbb megoldás
my_sum = 0
for element in my_list2:
    my_sum += element
print(my_sum)