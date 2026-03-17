
num = int(input("Enter number:"))
number = num

rev = 0

while num != 0:
    ls_dt = num % 10
    rev = rev * 10 + ls_dt
    num = num // 10
if number == rev:
    print(number,"is palindrome.")
