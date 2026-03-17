
def is_fibanocci_number(number):

    is_fibo = False
    prev = 0
    curr = 1
    if number == 0 or number == 1:
        is_fibo = True
    next = prev + curr
    while(next <= number):
        next = curr + prev
        prev = curr
        curr = next
        if next == number:
            is_fibo = True
            break
    return is_fibo

print(is_fibanocci_number(9))
print(is_fibanocci_number(5))
print(is_fibanocci_number(0))