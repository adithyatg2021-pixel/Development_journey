
num = int(input("Enter number:"))

number = num

result = 0

while(num != 0):
    digit = num % 10
    result = result * 10 + digit
    num = num // 10
if number == result:
    print(number,"is palindrome")
else:
    print(number,"is not palindrome")