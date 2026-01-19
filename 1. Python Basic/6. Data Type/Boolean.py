
# In programming you often need to know if an expression is True or False.

a = 9
b = 4

print(a>b)
print(a<b)
print(a==b)

#Using if else
if a<b:
    print("B is getter than A")
else:
    print("A is getter than B")



# When Come true:
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#When Come False:
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
print(bool(""),bool(()),bool([]),bool({}))


# Function can return true or False

def myFunc():
    a= 4
    b= 6
    return a<6

if myFunc():
    print("A is less than B")
else:
    print("B is less than A")
