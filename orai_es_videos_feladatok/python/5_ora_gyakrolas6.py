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