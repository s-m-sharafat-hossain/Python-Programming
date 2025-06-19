import operator

a = 10
b = 3

print("Addition:", operator.add(a, b))
print("Subtraction:", operator.sub(a, b))
print("Multiplication:", operator.mul(a, b))
print("Division:", operator.truediv(a, b))
print("Floor Division:", operator.floordiv(a, b))
print("Modulus:", operator.mod(a, b))
print("Power:", operator.pow(a, b))

print("Equal:", operator.eq(a, b))
print("Not Equal:", operator.ne(a, b))
print("Greater Than:", operator.gt(a, b))
print("Less Than:", operator.lt(a, b))

x = True
y = False
print("Logical AND:", operator.and_(x, y))
print("Logical OR:", operator.or_(x, y))

my_list = [1, 2, 3, 4]
get_item = operator.itemgetter(2)
print("Item at index 2:", get_item(my_list))

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
get_name = operator.attrgetter('name')
print("Person's name:", get_name(p))
