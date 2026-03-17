m1 = int(input("Enter mark 1 (Out of 50):"))
m2 = int(input("Enter mark 2 (Out of 50):"))
m3 = int(input("Enter mark 3 (Out of 50):"))

total = m1 + m2 + m3

total = total + (total * (2/100)) # 2% grace mark added

if total > 140: # No need of and condition
    print("A Grade")
elif total > 130:
    print("B grade")
elif total > 120:
    print("C grade")
else:
    print("Failed")