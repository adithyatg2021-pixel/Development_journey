num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

(large,small) = (num1,num2) if num1 > num2 else (num2,num1)

i = 1
while(True):
    result = large * i

    if result % small == 0:
        lcm = result
        break
    i = i + 1

print(f"Least common multiplier of {num1} and {num2}: {lcm}")
    
    

