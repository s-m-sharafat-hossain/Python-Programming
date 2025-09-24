
# Creating Variable:
# -> Python has no command for declaring variable.

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

x,y,z= fruits

print(x,y,z);



