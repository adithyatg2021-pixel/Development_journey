"""
receives any nummber of parameters as dictionary
while calling the function, the value should be passes as key = value
"""

def employee(**kwargs:dict): # {"name":"Vipin","dept":"hr","salary":25000}
    print(kwargs)
    print(kwargs.get("name")) # Vipin

employee(name = "Vipin",dept = "hr",salary= 25000)
employee(name = "Hari",dept = "qa",salary= 22000,age = 25)
