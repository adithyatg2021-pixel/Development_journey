num = int(input("Enter number:"))

perfect = 1

for i in range(2,num):
    if num % i == 0:
        perfect = 0
if perfect == 1:
    print(num,"is prime.")
else:
    print(num,"is not prime.")

