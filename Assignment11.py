# Lambada Function

# Syntax 
# variable = lambda parameter : operation

add = lambda a,b: a+b

print(add(2,3))

# Function with Default Parameters

def greet(name, greeting="Hello"):
   
    return f"{greeting}, {name}!"

# Calling the function with both parameters
print(greet("Alice", "Hi"))  # Output: Hi, Alice!

# Calling the function with only the name parameter
print(greet("Bob"))  # Output: Hello, Bob!