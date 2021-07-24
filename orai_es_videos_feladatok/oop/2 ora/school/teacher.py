"""

 * Öröklődéssel hozz létre két új osztályt, Teacher and CollegeStudent.
 *
 * A Teacher olyan, mint a Person, csak van két újabb properity-je:
 *  - salary (float)
 *  - subject (String)
 *  Használj toString metódust az összes class-ra.
 *
"""

from person import Person


class Teacher(Person):

    def __init__(self, name, age, gender, salary, subject):
        super().__init__(name, age, gender)
        self.salary = salary
        self.subject = subject

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} and i am {self.gender} and my salary " \
               f"is {self.salary} and my subject is {self.subject}"
