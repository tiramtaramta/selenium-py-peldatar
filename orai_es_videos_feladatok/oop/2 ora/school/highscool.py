"""
 Itt példányosítjuk és ellenőrizzük, hogy minden jó-e
"""

from college_student import CollegeStudent
from person import Person
from student import Student
from teacher import Teacher

person = Person("Olga", 12, "F")
student = Student("Agnes", 24, "F", "BDC234ASD", 2.2345)
teacher = Teacher("Kevin", 54, "M", 150.000, "History")
col_student = CollegeStudent("Tomislav", 30, "M", "ABGF342", 4.5, 2, "History")


# a toString azért kellett, hogy itt egyszerűen ki tudjuk printelni
print(person)
print(student)
print(teacher)
print(col_student)