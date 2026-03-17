class Person:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def display(self):
        print(f"Name of the person:{self.name}")
        print(f"City of the person:{self.city}")

person1 = Person("Hari","Thrissur")
person1.display()