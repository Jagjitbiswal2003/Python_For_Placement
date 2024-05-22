# raise Exception

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise Exception("You must be at least 18 years old.")
    else:
        return "Age is valid."


try:
    print(check_age(25))  
    print(check_age(-4))  
except ValueError as ve:
    print(f"Caught a ValueError: {ve}")
except Exception as e:
    print(f"Caught an Exception: {e}")
