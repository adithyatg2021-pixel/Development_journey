temp = int(input("Enter temperature:"))

if temp > 30:
    print("Temperature -> Hot")
elif temp <= 30 and temp >= 20:
    print("Temperature -> Wram")
else:
    print("Temperature -> Cold")