# List

# Python Set Operations

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding an element to a set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from a set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Discarding an element (no error if element not found)
my_set.discard(10)  # Trying to discard an element not present in the set
print("Set after discarding an element (10):", my_set)

# Creating another set
another_set = {4, 5, 6, 7, 8}
print("Another set:", another_set)

# Union of two sets
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection of two sets
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference of two sets
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Symmetric difference of two sets
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of sets:", symmetric_difference_set)

# Checking if a set is a subset of another
is_subset = {1, 2}.issubset(my_set)
print("Is {1, 2} a subset of my_set?", is_subset)

# Checking if a set is a superset of another
is_superset = my_set.issuperset({1, 2})
print("Is my_set a superset of {1, 2}?", is_superset)

# Checking if two sets are disjoint
are_disjoint = my_set.isdisjoint({10, 11})
print("Are my_set and {10, 11} disjoint?", are_disjoint)

# Clearing a set
my_set.clear()
print("Set after clearing:", my_set)

# Frozen set (immutable set)
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen_set)
