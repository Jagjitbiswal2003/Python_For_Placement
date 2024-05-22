# Polymerphisim

# Method Overloading :
# Python does not support method overloading in the traditional sense (like Java or C++). However, you can achieve similar functionality using default arguments or variable-length arguments.

class Vehicle:
    def start(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def start(self):
        return "Car engine started"

class Bike(Vehicle):
    def start(self):
        return "Bike engine started"

class Truck(Vehicle):
    def start(self):
        return "Truck engine started"

def start_vehicle(vehicle):
    print(vehicle.start())

car = Car()
bike = Bike()
truck = Truck()

start_vehicle(car)   # Output: Car engine started
start_vehicle(bike)  # Output: Bike engine started
start_vehicle(truck) # Output: Truck engine started
