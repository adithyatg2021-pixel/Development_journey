password = input("Enter password:")

if len(password) < 6:
    raise Exception("Invalid password...")
else:
    print("Password created successfully...")