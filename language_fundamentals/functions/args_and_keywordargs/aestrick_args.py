"""
*args -> receives any number of parameters as tuple, It is using instead of the concept of method over loading
"""

def add(*args): # (10,20)
    return sum(args)

print(add(10,20))   # 30
print(add(10,20,30))    # 60

def largest_number(*args):
    return max(args)

print(largest_number(10,20,30,5))
print(largest_number(10,20,30,5,78))

