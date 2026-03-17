def leap_year(year):
    if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")

leap_year(1780)
leap_year(1997)