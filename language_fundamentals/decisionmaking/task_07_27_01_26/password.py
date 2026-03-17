password = input("Enter password:")

length = len(password)

if length >= 8:
    print("Login successfull")
else:
    print("Invalid password")