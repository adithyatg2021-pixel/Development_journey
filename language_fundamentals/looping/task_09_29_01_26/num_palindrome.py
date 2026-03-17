num = int(input("Enter number:"))
count = 0
i = 1
flag = 0
number = num
l = 0
f = 0
count = len(str(num))

while(count != 0):
    l = number % (10 ** i)
    number = number // 10
    i += 1
    f = num // (10 ** (count - 1))
    num = num % (10 ** (count - 1))
    if l == f:
        count -= 1
        flag = 1
    else:
        break

if flag == 1:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")
    


    
    
        
    



