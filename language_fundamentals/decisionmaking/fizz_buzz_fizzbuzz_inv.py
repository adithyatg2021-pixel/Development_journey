num = int(input("Enter number:"))

if num % 15 == 0:
    print("FIZZBUZZ")
elif num % 5 == 0:
    print("BUZZ")
elif num % 3 == 0:
    print("FIZZ")
else:
    print("INVALID...")


"""
in the if elif block which condition become true first it will execute and exit from the loop.
"""