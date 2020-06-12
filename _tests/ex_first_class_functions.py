from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 10, operator=divide)
print(result)


friends = [
    {'name': 'Rolf Smith', 'age': 24},
    {'name': 'Adam Coll', 'age': 30},
    {'name': 'Anne Pun', 'age': 27},
]

def search(sequence, attr, expected, finder):
    for elem in sequence:
        if finder(elem, attr) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

def search_two(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

def get_data_attr(data, attr):
    return data[attr]


print( 'normal test', '->', search(friends, 'age', 30, get_data_attr) )
print( 'with lambda', '->', search_two(friends, 'Anne Pun', lambda friends: friends['name']) )
print( 'with itemgetter', '->', search_two(friends, 24, itemgetter('age')) )
