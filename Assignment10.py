# *args use
def sum_numbers(*args):
  
    # args is a tuple containing all the positional arguments passed to the function
    return sum(args)  # sum() calculates the total sum of the elements in args

# Example calls and their outputs:
print(sum_numbers(1, 2, 3)) 
print(sum_numbers(4, 5))     

# **kwargs use
def print_details(**kwargs):
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
print_details(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York