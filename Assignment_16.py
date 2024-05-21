# List Methods

lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]

lst = [1, 2, 3]
lst.insert(1, 4)
print(lst)  # Output: [1, 4, 2, 3]

lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)  # Output: [1, 3, 2]

lst = [1, 2, 3]
lst.pop()
print(lst)  # Output: [1, 2]

lst = [1, 2, 3]
print(lst.index(2))  # Output: 1

lst = [1, 2, 2, 3]
print(lst.count(2))  # Output: 2

lst = [3, 1, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3]

lst = [1, 2, 3]
lst.reverse()
print(lst)  # Output: [3, 2, 1]

lst = [1, 2, 3]
lst.clear()
print(lst)  # Output: []
