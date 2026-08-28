
# -> Python has no command for declaring variable.

'''                      Python Variables:

=> Rules for Python Variables:
1. A variable name must start with a letter or the underscore character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
4. Variable names are case-sensitive.
5. A variable name cannot be any of the Python reserved words.

=> Creating a Variable:

-> Example:
x = 5
y = "Hello World"
z = 5.6

a=b=c=5

a = [1,2,3]   #List
b = (1,2,3)   #Tuple
c = {1,2,3}   #Set
d = {'name':'Sharafat', 'age':24}   #Dictionary
'''

'''                      Variable Case:
-> There are different cases to name a variable:
1. Camel Case: myVariableName
2. Pascal Case: MyVariableName
3. Snake Case: my_variable_name
'''



x=5
a="Sharafat Hossain"
y=5.6

print(x)
print(y)
print(a)


# Type Casting:
# -> If I want to specify the type of variable, this can done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x,y,z)


# Get the Type:
# -> I can get data type of a variable with the type() function.

x = 5
y = "Sharafat"

print(type(x))
print(type(y))


# Single or Double quotes "",'' are same.
# Variable names are case-sensitive.
# Variable name not allow like this: 2myvar, my-var, my var

# Some variable case:
# -> Camel Case: myVariableName.
# -> Pascal Case: MyVariableName.
# -> Snake Case: my_variable_name.


# Multiple Values and Variable

x, y, z = 3, 4, 5

print(x,y,z)

# One value to multiple Variable
x=y=z=5

print(x,y,z)

# Unpack a Collection:
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ['apple','banana','cherry']

x,y,z= fruits   # x=apple, y=banana, z=cherry

print(x)
print(y,z)



