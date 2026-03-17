
def factorial(num):
    product = 1
    for i in range(1,num+1):
        product = product*i
    return product
print("Factorial of 7 is:",factorial(7))
        