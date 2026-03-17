num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

gcd = 1

smallest = num1 if num1 < num2 else num2 # meaning = return num1 if num1 < num2 else return num2 

for i in range(1,smallest+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(f"Greatest common divisor of {num1} and {num2} is {gcd}")
