character = input("Enter the character:")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

if character in upper:
    print(character,"is in UPPERCASE")
else:
    print(character,"is in LOWERCASE")