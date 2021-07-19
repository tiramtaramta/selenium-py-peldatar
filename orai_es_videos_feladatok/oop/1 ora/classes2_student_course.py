# egy file-ban egy class van!!!
class Student:
    # tanuló konstruktora (név, kor, minősítés)
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    # visszaadja a beadott objektum grade-jét (getter -> bármilyen tulajdonság elkérése önmagától)
    def get_grade(self):
        return self.grade

    def get_age(self):
        return self.age


class Course:
    # a kurzus konstruktora (neve és a max létszám)
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students  # tanulók maximális száma
        self.students_list = []  # üres lista (nincsenek benne tanulók)

    # adott kurzushoz hozzáadunk egy tanulót
    def add_student(self, student):
        if len(self.students_list) < self.max_students:  # limitálva van a tanulók száma. megvizsgálja és ha még befér...
            self.students_list.append(student)  # hozzáadja a listához
            return True  # ha hozzáadta a return True
        else:
            return False

    # a kurzus átlagát számoltatjuk ki
    def get_average_grade(self):
        value = 0  # nulláról indulunk
        for student in self.students_list:
            value = value + student.get_grade()
        return value / len(self.students_list)  # az érték elosztva a lista hosszával


# létrehozunk 3db tanulót
s1 = Student("Tim", 19, 30)
s2 = Student("Bill", 19, 70)
s3 = Student("Jill", 19, 10)

# max 2 db tanulóval létrehozunk egy science nevű kurzust
course = Course("Science", 2)
print(course.add_student(s1))  # a return értékeket printeltetjük ki (true/false)
print(course.add_student(s2))
print(course.add_student(s3))

# a gettereket meg tudom hívni az adott tanuló változóján
print(s2.get_age())
print(s3.get_grade())

# a kurzus átlagszámításának metódusát meghívjuk
print(course.get_average_grade())
