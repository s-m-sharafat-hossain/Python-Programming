"""Python practice: Python Basic / Input Output / Input. Short example for learning Python."""

# Basic input
name = input("Enter your name: ")
print("Hello,", name)

# Integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Float input
price = float(input("Enter the price: "))
print("Price is:", price)

# Multiple inputs: in String format
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

# Converting multiple inputs to integers
a, b = map(int, input("Enter two integers: ").split())
print("Sum:", a + b)

# Converting multiple inputs to floats
p, q = map(float, input("Enter two float numbers: ").split())
print("Product:", p * q)

# Using a different separator
data = input("Enter values separated by commas: ").split(',')
print("You entered:", data)