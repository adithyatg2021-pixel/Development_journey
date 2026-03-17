class GrandParent:
    def properties(self):
        print("Grand parent properties method")
class Parent(GrandParent):
    def house(self):
        print("Parent house method")
class Child(Parent):
    pass

child_instance = Child()
child_instance.properties()
child_instance.house()