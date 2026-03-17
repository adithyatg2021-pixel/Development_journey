# function with no parameter and no return value

"""
def function_name(p1,p2):
    body

function_name(srg1,arg2)
"""


# def addition(num1,num2):
#     addition = num1+num2
#     print(f"{num1} + {num2} = {addition}")

# addition(200,600)
# addition(500,700)

# here 2 paramaters are defined. So, we need to pass 2 argumnets

# def sub(num1,num2):
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")

# sub(400,100)
# sub(100,200)



"""
above 2 functions are defined with same parameter value. But the parameters have their scope 
only with in that function

"""

def cube(num):
    result = num ** 3
    print(f"{num}^3 = {result}")

cube(2)