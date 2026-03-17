num = int(input("Enter number:"))

sum = 0

number = num

while(num != 0):
    last_digit = num % 10
    sum += last_digit
    num = num // 10
print("Sum of digits in",number,":",sum)