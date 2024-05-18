# If-else 

# Syntax 
# if condition:
    # code block
# elif another_condition:
    # another code block
# else:
    # else code block
    
# Max of 3 numbers using nested if-else

print("Enter three numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)

