# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing a value
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating a value
my_dict["age"] = 31

# Removing a key-value pair
del my_dict["city"]

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "email" in my_dict:
    print("Email exists in the dictionary")
