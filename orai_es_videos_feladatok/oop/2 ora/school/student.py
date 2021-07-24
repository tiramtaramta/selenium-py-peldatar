"""
 * Hozz létre egy Person superclass-t és egy Student subclass-t.

 * A Student-nek két attribútuma van:
 *  - idNumber (String)
 *  - gradePointAverage (float)
 *  Használj toString metódust az összes class-ra.
 *
"""
from person import Person


class Student(Person):

    def __init__(self, name, age, gender, id_number, grade_point_average):
        super().__init__(name, age, gender)
        self.id_number = id_number
        self.grade_point_average = grade_point_average

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} and i am {self.gender}. "\
               f"My ID number: {self.id_number} and my avg grade point: {self.grade_point_average}"
