side1 = int(input("Enter the length side 1 of triangle:"))
side2 = int(input("Enter the length side 2 of triangle:"))
side3 = int(input("Enter the length side 3 of triangle:"))

if side1 == side2 == side3:
    triangle = "e"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle = "i"
elif side1 != side2 != side3:
    triangle = "s"

match triangle:
    case "e":
        print("Equilateral")
    case "i":
        print("Isosceles")
    case "s":
        print("Scalene")