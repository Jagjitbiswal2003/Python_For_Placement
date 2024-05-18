# Swap 3 values using third variable and using mathematic operation

print("Enter three numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Swapping using a third variable
temp = a
a = b
b = c
c = temp

print(a,b,c)

# Swapping using arithmetic operations

#a = a + b + c
#b = a - (b + c)
#c = a - (b + c)
#a = a - (b + c)

#print(a,b,c)


# The two methods give different results because the arithmetic operations do not properly swap the values. The correct method using a third variable correctly rotates the values, while the arithmetic method ends up with a different set of values that doesn't achieve the intended swap.