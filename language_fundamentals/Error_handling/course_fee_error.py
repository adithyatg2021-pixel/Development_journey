"""
Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally

"""

name = input("Enter name:")

try:
    course_fee = int(input("Enter course fee:"))
    paid_amount = int(input("Enter paid amount:"))

    if course_fee < 0:
        raise Exception("Invalid enter for course fee. Fee cannot be negative.")
    if paid_amount < 0:
        raise Exception("Invalid enter for amount paid. Amount cannot be negative.")
    if paid_amount > course_fee:
        raise Exception("Paid amount is greater than course fee..")
    
except Exception as e:
    print(e)

finally:
    print("Registraion process finished...")