"""
Assert used for debugging code
assert key word used for making a condition, if the condition failed it will raise debug message. 

Syntax

assert condition,message
"""
def cube(num):
    result = 0

    # Enter your code here

    result = num ** 3

    return result

assert cube(5) == 125,"Test case 1 failed..."
assert cube(2) == 8,"Test case 2 failed..."

print("Code accepted...")