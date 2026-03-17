
def amstrong(num):

    number = num

    sum = 0

    digit_count = len(str(num))

    while(num != 0):
        l_d = num % 10
        sum += l_d ** digit_count
        num = num // 10

    if sum == number:
        print(f"{number} is amstrong.")
    else:
        print(f"{number} is not amstrong")

amstrong(153)
amstrong(152)