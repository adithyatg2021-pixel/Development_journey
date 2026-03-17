class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee name:{self.name}")
        print(f"Employee salary:{self.salary}")

employee1 = Employee("Arun",25000)
employee1.display()