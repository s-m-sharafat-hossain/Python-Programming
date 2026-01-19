                            # AND

a = 5;
b = 3;
c = 5;

if a>b and a==c:
    print("A is Greater than B and equal to C")
elif b<c and a==c:
    print("B is less than C and C is equal to A")
else:
    print("Not valid")

                            # OR


if a>b or a==c:
    print("A is Greater than B and equal to C")
elif b<c or a==c:
    print("B is less than C and C is equal to A")
else:
    print("Not valid")


                            # Not

if not b>a:
    print("B is not greater than A")