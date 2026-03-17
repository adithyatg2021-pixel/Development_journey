db_username = "Abcd@345"
db_password = "password@56"

username = input("Enter username:")
password = input("Enter password:")

if username == db_username and password == db_password:
    print("Login successfull")
else:
    print("Invalid credentials")