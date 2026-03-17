
def last_digit_max(num1,num2):
    last_digit_num1 = num1 % 10
    last_digit_num2 = num2 % 10

    print(num1 if last_digit_num1 > last_digit_num2 else num2)

last_digit_max(98,123)
last_digit_max(125,343)
