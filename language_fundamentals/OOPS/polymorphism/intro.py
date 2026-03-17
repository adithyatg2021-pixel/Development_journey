"""
more than one form

2 types
1) method overloading
2) method overriding

"""

# method overloading -  same class have more than one method with same name and different number pf parameters

# it is not supported by python

# instead we use *args and **kwargs

class Calculator:

    def add(self,n1,n2):
        return n1 + n2
    def add(self,n1,n2,n3):
        return n1 + n2 + n3
    def add(self,n1,n2,n3,n4):
        return n1 + n2 + n3 + n4  # in the memory only the last add method is exising
    
calc_instance = Calculator()
print(calc_instance.add(10,20,30,40)) # 100

# print(calc_instance.add(10,20,30)) # error - the method with 4 arguments is existing in memory
