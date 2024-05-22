
# Encapsulation


class Person:
    def __init__(self, name, age, salary):
        self.name = name      
        self.age = age      
        self.salary = salary 
        self.emp_details={    # Private
            "Name:":"Jagjit",
            "Address:":"abs",
            "MobileNo:":2134567893
        }
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        

p1 = Person("Jagjit",21,20000)
p1.show()
