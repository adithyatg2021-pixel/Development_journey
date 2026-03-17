
def prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    return is_prime

print(prime(5))
print(prime(10))