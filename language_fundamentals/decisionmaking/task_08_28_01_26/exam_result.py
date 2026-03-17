db_roll_no = range(1,51)

roll_no = int(input("Enter your roll number:"))

if roll_no in db_roll_no:
    marks = int(input("Enter marks:"))

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid roll number")