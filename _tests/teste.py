class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'Person {}, {} years old'.format(self.name, self.age)
    
    def __repr__(self):
        return '<Person({}, {})>'.format(self.name, self.age)


bob = Person('bob', 33)
print(bob)
bob.__repr__()