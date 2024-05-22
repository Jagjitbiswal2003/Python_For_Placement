# Class and Objects

class Student:
 
   # Constructor
   def __init__(self, name, age):
       self.name = name
       self.age = age
       
   # Method to print student details
   def print(self):
       print("Name:", self.name)
       print("Age:", self.age)
        
# Create an instance of Student
st1 = Student("Jagjit", 21)
st1.print()    # Call the print method
