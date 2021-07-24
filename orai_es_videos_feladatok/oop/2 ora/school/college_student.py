"""
 * Hozz létre egy Person superclass-t és egy Student subclass-t.
 * A CollegeStudent class kiterjeszti Student class-t az alábbi properity-vel
 *  - year (int)
 *  - major (String)
 *
 *  Használj toString metódust az összes class-ra.
 *
"""
from student import Student
from person import Person


class CollegeStudent(Student):

    def __init__(self, name, age, gender, id_number, grade_point_average, year, major):
        super().__init__(name, age, gender, id_number, grade_point_average)
        self.year = year
        self.major = major

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} and i am {self.gender}. "\
               f"My ID number: {self.id_number} and my avg grade point: {self.grade_point_average}, " \
               f"My major is {self.major} and i am in {self.year}"