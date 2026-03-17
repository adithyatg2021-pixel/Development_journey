num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 < num2:
    for i in range(1,num1+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
else:
    for i in range(1,num2+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
print("GCD:",gcd)