num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 < num2:
    limit = num1
else:
    limit = num2

for i in range(1,limit+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)

