from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('Bob')
ana = Student('Ana')

bob.take_exam(90)
# ana.take_exam(50)
# ana.take_exam(30)

print(bob.grades)
print(ana.grades)