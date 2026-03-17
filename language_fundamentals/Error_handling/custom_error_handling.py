"""
To customize exception handling
'raise' is the keyword used for creating custom errors
"""

age = int(input("Enter age:"))

if age < 18:

    raise Exception("Invalid age..")

else:
    print("Access granted..")