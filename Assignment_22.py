# Inheritance

class Person:
    
    def __init__(self,name):
        self.name = name
        
    def check(self):
        print("Inherit the Person class")
        
        
class Ram(Person):   # Ram inherit the person class
      
       def __init__(self,name,age,salary):
           super().__init__(name)
           self.age = age
           self.salary = salary
           
       def inherit(self):
        print("Name:",self.name)
        print("Inheritance Successful")
        
        
r1 = Ram("Jagjit",21,23333)
r1.inherit()
r1.check()