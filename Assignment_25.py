# try and multiple except in python

# else block will execute when there is no exception in try block
# Syntax
# try:
    # Code that might raise an exception
   
# except SomeException as e:
    # Code that runs if an exception occurs
    
# else:
    # Code that runs if no exception occurs
  
# finally:
    # Code that always runs, regardless of exceptions
  

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return f"The result is {result}"
   

print(divide_numbers(10, 2))  # Expected: The result is 5.0
print(divide_numbers(10, 0))  # Expected: Error: Division by zero is not allowed.
print(divide_numbers(10, 'a'))  # Expected: Error: Both arguments must be numbers.
