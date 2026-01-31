# Python Operator:

# Arithmetic operators:     +, -, *, /, %, **(Exponentiation), //(Floor Division)
a = 45
b =34
print(a+b, a-b, a*b, f"{a/b:.2f}", a%b, a//b)
# a**b like a^b
print(2**3)
#Floor division means: if 15/2 = 7.3434 it take 7 (floor value)
print(13//2)




# Assignment operators:     +=, -=, *=, /=, %=, //=, **=
a=5;
a+=4
print(a) #It means: a= a+4

a/=2
print(f"{a:.2f}")

a=43
a//=4
print(a)



# Comparison operators:     ==, !=, >, <, >=, <=
a=5
b=6
print(a>b , a<b, a==b, a!=b)    #Output: true or false




# Logical operators:        and, or, not
x =5
print(x>3 and x<10)

print(x<4 or x>12)

print(not(x>3 and x<10))    #Change output



# Identity operators:       is, is not
# Basically use in Condition.

a= 5 
b= 5
if a is b:
    print("A = B")    
if a is not b:
    print("A!=B")
b=6
print(a is b)


# Membership operators:     in, not in
# Us in loop and check 
x = ["apple", "banana"]
print("banana" in x)

x = 5
for i in range(x):
    print("Number: ",i)

for i in range(5):
    print("Number: ",i)

# Use not in
x = ["apple", "banana"]
print("cherry" not in x)  # print Boolean value True.


# Bitwise operators:        &(AND), \(OR), ^(XOR), ~(Not)

a = 10   # binary: 1010
b = 4    # binary: 0100

print("a & b =", a & b)   # 1010 & 0100 = 0000 -> 0
print("a | b =", a | b)   # 1010 | 0100 = 1110 -> 14
print("a ^ b =", a ^ b)   # 1010 ^ 0100 = 1110 -> 14
print("~a =", ~a)         # ~1010 = -(10+1) -> -11
