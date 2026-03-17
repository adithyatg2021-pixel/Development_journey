"""
child class redefines the method that is already defined in parent class. The signature of the method should be same.
Signature means, the name of the method and the number of parameter.
Overriding is used when the method inside parent class needs a new definition.
"""

class Parent:
    def vehicle(self):
        print("Passion Pro")
    def car(self):
        print("Swift")

class Child(Parent):
    def vehicle(self):
        print("Gurilla 450")
    def car(self):
        print("Balano")
child_instance = Child()
child_instance.vehicle() # Gurilla 450
child_instance.car() # Balano