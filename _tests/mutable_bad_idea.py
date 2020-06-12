from typing import List


class Student:
    """
    Como a lista é um objeto mutavel quando criados os dois objetos
    eles apontam para a mesma lista e ao adicionar uma nota na lista
    de um aluno ela tambem aparece na lista de outros alunos criados
    pois o método está referenciando a mesma lista que foi criada no 
    início
    """
    # def __init__(self, name: str, grades: List[int] = []): # Nào fazer isso
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []
        # self.grades = grades # Nào fazer isso
    
    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('Bob')
ana = Student('Ana')

bob.take_exam(90)
# ana.take_exam(50)
# ana.take_exam(30)

print(bob.grades)
print(ana.grades)