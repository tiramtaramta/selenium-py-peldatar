class Student:
    def __init__(self, _subjects):
        self.subjects = _subjects

    def __str__(self):
        return str(self.subjects)


students = {}
with open("file_osszetett_adatok.txt", "r") as file:  # file a file változó neve
    num_students = int(file.readline().strip())  # az első sor tartalmazza, hogy hány tanuló van a dokumentumban
    for i in range(num_students):  # addig a számig megy a for ciklus
        name = file.readline()  # első tanuló neve
        num_subject = int(file.readline().strip())  # következő sor tartalmazza, hogy hány tantárgya van
        student_subjects = {}
        for j in range(num_subject):  # addig a számig megy a for ciklus
            subject_name = file.readline().strip()  # beolvassuk az első tantárgy nevét
            subject_grades = file.readline().strip().split(",")  # majd a hozzá tartozó jegyeket
            student_subjects[subject_name] = subject_grades  # a tárgy kulcshoz tartoznak a jegyek
        students[name] = Student(student_subjects)  # a tanuló nevéhez tartoznak az osztály tárgyai

for k, v in students.items():
    print(k, v)


