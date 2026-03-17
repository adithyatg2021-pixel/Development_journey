number = int(input("Enter number:"))

sum = 0

for i in range(1,number):
    if number % i == 0:
        sum += i
print(f"{number} is perfect number" if number == sum else f"{number} is not perfect number")