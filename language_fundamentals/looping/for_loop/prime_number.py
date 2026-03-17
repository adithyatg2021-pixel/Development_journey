number = int(input("Enter number:"))

# is_prime = True

# for i in range(2,number):
#     if number % i == 0:
#         is_prime = False
#         break
# print(is_prime)
if number == 2:
    print(number,"is prime")

for i in range(2,number):
    if number % i == 0:
        print(number,"is not prime")
        break
    else:
        print(number,"is prime")