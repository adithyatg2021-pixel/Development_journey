class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student name:{self.name}")
        print(f"Student age:{self.age}")

student1 = Student("Hima",24)
student1.display()
