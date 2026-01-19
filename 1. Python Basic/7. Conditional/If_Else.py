
# Using if keyword we can state all mathematical condition. Like:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 55
b = 34
if a>b:
    print("A is Getter than B")

# Indentation: Whitespace at the beginning of the line.

if a>b:
    print("A is greater than B")
else:
    print("B is greater than A")

                                # Elif

# Short form of Else if. if the previous conditions were not true.

if a>b:
    print("A is greater than B")
elif a==b:
    print("B is equal to A")
else:
    print("B is greater than A")


                            # Short Hand

if a>b: print("A is greater than B")

print("A") if a>b else print("B")