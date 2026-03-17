
"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists

"""

student = {"id":25,"Name":"Anamika","Course":"Python Django","Marks":86}

print(student["Name"])

student["Marks"] += 5

student["Grade"] = "A"

print(student)

if "attendance" in student:
    print("Key exists.")
else:
    print("Not exists.")