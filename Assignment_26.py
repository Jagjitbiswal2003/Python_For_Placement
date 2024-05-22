# Finally block : it will always execute and it doesnot depends on the exception that occur in try block

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
    finally:
        print("Execution completed.")

# Test cases
print(divide_numbers(10, 2))  # Expected: The result is 5.0
print(divide_numbers(10, 0))  # Expected: Error: Division by zero is not allowed.
print(divide_numbers(10, 'a'))  # Expected: Error: Both arguments must be numbers.
