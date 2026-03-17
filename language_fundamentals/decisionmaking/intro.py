"""
decision making statesments are use to perform actions based on certain condition

syntax: 
if condition:
    stmnt 1
    stmnt 2
else:
    stmt 1
    stmt 2

input -> read value through console, value is string
"""

number = int(input("Enter number:")) # input function is used to get user data. It recieves data as string.
                                     # "int" keyword is used to convert the data in string to integer
if number == 0: 
    print("Number is zero")

else:
    print("Non - zero number")

