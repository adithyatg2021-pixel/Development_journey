
def is_odd(num):

    return True if num % 2 != 0 else False

print("Is number odd?",is_odd(45))
print("Is number odd?",is_odd(24))


print("==========================")

def is_even(num):
    # return True if num % 2 == 0 else False
    return num % 2 == 0

print("Is number even?",is_even(64))
print("Is number even?",is_even(25))


print("==========================")


def is_positive(num):
    return True if num > 0 else False

print("Is number positive?",is_positive(-34))

print("==========================")

def is_zero(num):

    # return True if num == 0 else False 
    return num == 0

print("Is number zero?",is_zero(45))