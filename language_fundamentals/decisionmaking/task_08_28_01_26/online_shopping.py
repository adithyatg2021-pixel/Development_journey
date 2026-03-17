db_coupen_code = 7890

coupen_code = int(input("Enter coupen code:"))

if db_coupen_code == coupen_code:
    cart_amount = int(input("Enter cart amount:"))
    if cart_amount >= 1000:
        print("Coupon applied")
    else:
        print("Minimum purchase not met")
else:
    print("Invalid coupon")