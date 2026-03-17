
"""
Anonymous function with single expression
Syntax:
var_name = lambda p1,p1,....:expression
"""

# def add(n1,n2):
#     return n1+n2

# using lambda function

add = lambda n1,n2:n1+n2

print(add(100,200))

sub = lambda n1,n2:n1-n2

print(sub(100,30))

cube = lambda n:n**3

print(cube(3))

odd_even = lambda num : "Even number" if num % 2 == 0 else "Odd number"

print(odd_even(25))

# number is positive or not

is_positive = lambda num : True if num > 0 else False
is_positive = lambda num : num > 0 

print(is_positive(-4))