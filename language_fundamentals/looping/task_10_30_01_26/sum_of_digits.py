num = int(input("Enter number:"))

number = num
sum = 0

while(num != 0):
    last_digit = num % 10
    sum += last_digit
    num = num // 10
print("Sum of digits in",number,":",sum)
