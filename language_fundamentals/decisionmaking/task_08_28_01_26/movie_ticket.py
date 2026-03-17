age = int(input("Enter age:"))
seat_availability = 42

if age >= 18:
    seats = int(input("Enter the required number of seats:"))

    if seats <= seat_availability:
        print("Ticket booked") 
    else:
        print("House full")
else:
    print("Not eligible to watch the movie.")

