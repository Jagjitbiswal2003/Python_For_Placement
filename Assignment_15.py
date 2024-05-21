# List and List Input

# Initialize an empty list to store user input
user_list = []

while True:
    element = input("Enter an element (or type 'done' to finish): ")
    
    # Check if the user typed 'done' (case insensitive)
    if element.lower() == 'done':
        # If they did, break out of the loop
        break
    
    # If they didn't type 'done', add the element to the list
    user_list.append(element)
    
print("The list is:", user_list)
# or

#for i in user_list:
#   print(i)
    
# OR

 # user input second method
 # Ask the user for input
# input_string = input("Enter the elements of the list, separated by spaces: ")

# Split the string into a list
# user_list = input_string.split()

# print("The list is:", user_list)

 # List Methods
 
 