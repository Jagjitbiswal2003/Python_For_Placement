# function in Python

#def function_name(parameters):
    # Function body
    # Your code here
# Fibonacci series

def fibonacci(num):
    a = 0
    b = 1
    print(a, b, end=' ')
    
    for i in range(2, num):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

num = 3
fibonacci(num)

    
    