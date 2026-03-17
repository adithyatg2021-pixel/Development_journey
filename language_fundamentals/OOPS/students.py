class Student:
    name:str
    course:str
    roll_num:int

    def __init__(self,name_of_student,course,roll):
        self.name = name_of_student
        self.course = course
        self.roll_num = roll

    def display(self):
        print(self.name,self.course,self.roll_num)

student1 = Student("Niya","Python",12)
student1.display()

student2 = Student("Praveen","Data analytics",33)
student2.display()