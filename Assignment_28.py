# File handling in Python

import os

def file_operations():
    # 1. Create and write to a file
    with open('example.txt', 'w') as file:
        file.write("This is an example file.\n")
        file.write("It contains multiple lines.\n")

    # 2. Read the file content
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content after writing:\n", content)

    # 3. Check if the file exists
    if os.path.exists('example.txt'):
        print("File exists")

    # 4. Get the file size
    size = os.path.getsize('example.txt')
    print(f"File size: {size} bytes")

    # 5. Append to the file
    with open('example.txt', 'a') as file:
        file.write("This line is appended to the file.\n")

    # 6. Read the file content again
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content after appending:\n", content)

    # 7. Rename the file
    os.rename('example.txt', 'example_renamed.txt')
    print("File renamed to 'example_renamed.txt'")

    # 8. Verify the renamed file exists
    if os.path.exists('example_renamed.txt'):
        print("Renamed file exists")

    # 9. Delete the file
    os.remove('example_renamed.txt')
    print("File 'example_renamed.txt' has been deleted")

    # 10. Verify the file has been deleted
    if not os.path.exists('example_renamed.txt'):
        print("File does not exist after deletion")

# Run the file operations
file_operations()
