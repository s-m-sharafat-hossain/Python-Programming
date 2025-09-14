# Build in data types:

#=> Text Type:      str
#=> Numeric Type:   int, float, complex
#=> Sequence Type:  list, tuple, range
#=> Mapping:        dict
#=> Set Type:       set, frozenset
#=> Boolean Type:   bool
#=> Binary Type:    bytes, bytearray, memoryview.
#=> None Type:      NoneType.

# In Python, the data type is set when you assign a value to a variable.

#String:
x = "Hello World"
y = str("Hello World")
print(x,y)

#Integer:
x = 50
y = int(5)
print(x,y)

#Floating:
x = 50.56
y = float(50.56)
print(x,y)

#Complex: Complex like 4+5j [j is complex part]
x = 5j
y = complex(5j)
print(x,y)

#List: use []
x = ['apple','cherry','banana']
y = list(('apple','cherry','banana'))
print(x,y)

#Tuple: like list use ()
x = ('apple','cherry','banana')
y = tuple(("apple","cherry","banana"))
print(x,y)

#Range: fixed array range
x = ('apple','cherry','banana')
y = range(5)
print(x,y)

#Dict: use {} 
x = {'Name':'Sharafat', 'Age': 34 }
y = dict({'Name':'Sharafat', 'Age': 34 })
print(x,y)

#Set: like list use {}
x = {'apple','cherry','banana'}
y = set({'apple','cherry','banana'})
print(x,y)

#Boolean:
x = True
y = bool(False)
print(x,y)

#Byte
x = b"Hello"
y = bytes(5)
print(x,y)

#ByteArray and MemoryView
y = bytearray(6)
z = memoryview(bytes(5))
print(y,z)

#None Type
x = None
print(x)



