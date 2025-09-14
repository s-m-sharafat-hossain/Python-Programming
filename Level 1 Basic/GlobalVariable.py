
# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = 'Sharafat'

def myFunction():
    x = 'hossain' #This is not work out of the function.
    print(x)

myFunction()

print("Output: "+x)


# Now using global keyword
x = 'Sharafat'

def myFunction():
    global x
    x = 'hossain' #Now it Change global x value.
    print(x)

myFunction()

print("Output: "+x)

# We can use it loop, oop etc



