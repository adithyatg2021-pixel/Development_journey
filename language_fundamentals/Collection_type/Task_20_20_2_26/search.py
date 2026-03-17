
se = {23,89,67,12,19,10}

num = int(input("Enter number to search:"))

present = 0

for n in se:
    if n == num:
        present = 1

if present == 1:
    print(num,"is present")
else:
    print(num,"is not present")