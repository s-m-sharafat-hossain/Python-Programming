
#Integer:
x = -50
y = int(5)
print(x,y)

#Floating:
x = 50.56
y = float(50.56)
print(x,y)

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 3.4e4
y = 4.5e-4
a = type(x)
print(x,y,a)

#Complex: Complex like 4+5j [j is complex part]
x = 3+5j
y = complex(5j)
print(x,y)

#Random Number
import random

x = random.randrange(1,10)
print(x)

# Type Casting:
x = int('4') # int convert string to integer.
y = 4
print(x+y) #result 8