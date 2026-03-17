class Parent:
    def house(self):
        print("Parent class house method.")

class Child(Parent): # Child is a Parent
    def mobile(self):
        print("Child class mobile method.")

child_instance = Child()
child_instance.mobile()
child_instance.house() # Accessing the method of parent class using child class instance.