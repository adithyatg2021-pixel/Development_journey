num1 = int(input("Enter number 1:")) #10

num2 = int(input("Enter number 2:")) #20

num3 = int(input("Enter number 3:")) # 30

if num1 > num2 and num1 > num3: # 10 >20 [F] and 10 > 30 [F]
    print(num1,"is greater.")
elif num2 > num1 and num2 > num3: #20 > 10[T] and 20 > 30 [F]
    print(num2,"is greater.")
else: #[T]
    print(num3,"is greater.")