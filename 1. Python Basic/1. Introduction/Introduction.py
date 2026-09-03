"""A short introduction to Python for beginners."""

# Python is a readable, general-purpose programming language.
# It is used for websites, automation, data analysis, and many other tasks.
# Python programs are executed from top to bottom.

# The print() function displays text on the screen.
print("Hello, Python!")

# Variables store values. Python determines the type automatically.
name = "Sharafat"
age = 20

print("My name is", name)
print("I am", age, "years old.")

# Python can perform calculations with numbers.
first_number = 10
second_number = 3
total = first_number + second_number

print("The total is", total)


def greet(person):
	"""Return a friendly greeting for a person."""
	return f"Welcome to Python, {person}!"


print(greet(name))

