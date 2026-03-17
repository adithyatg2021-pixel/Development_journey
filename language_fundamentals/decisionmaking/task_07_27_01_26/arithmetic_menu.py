
print("Arithmetic operations:")
print("1->Addition")
print("2->Subtraction")
print("3->Multiplication")
print("4->Division")
ch = int(input("Enter the choice:"))
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

match ch:
    case 1:print("Result of",num1,"+",num2,":",num1+num2)
    case 2:print("Result of",num1,"-",num2,":",num1-num2)
    case 3:print("Result of",num1,"*",num2,":",num1*num2)
    case 4:print("Result of",num1,"/",num2,":",num1/num2)
    




