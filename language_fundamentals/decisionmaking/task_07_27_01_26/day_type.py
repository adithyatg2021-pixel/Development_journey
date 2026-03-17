day = int(input("Enter day number:"))

if day in range(1,6):
    print("Working day")
elif day in range(6,8):
    print("Weekend")