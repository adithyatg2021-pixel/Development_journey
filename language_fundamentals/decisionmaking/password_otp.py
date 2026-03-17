
db_passowrd = "password@123"
db_otp = 2769

password = input("Enter password:")

if password == db_passowrd:
    otp = input("Enter OTP:")
    if otp == db_otp:
        print("Login successfull")
    else:
        print("Incorrect otp")
else:
    print("Incorrect password")