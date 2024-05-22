# Dictionary Method

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# get method
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("email", "Not Found"))  # Output: Not Found

# keys method
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# values method
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])

# items method
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# update method
my_dict.update({"email": "alice@example.com"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}

# pop method
print(my_dict.pop("age"))  # Output: 30
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

# popitem method
print(my_dict.popitem())  # Output: ('email', 'alice@example.com')
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# clear method
my_dict.clear()
print(my_dict)  # Output: {}

# copy method
new_dict = my_dict.copy()
print(new_dict)  # Output: {}
