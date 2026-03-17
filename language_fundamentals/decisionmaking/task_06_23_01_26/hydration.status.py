urine_color_scale = int(input("Enter urine color scale:"))

if urine_color_scale >= 1 and urine_color_scale < 4:
    print("Well hydrated")
elif urine_color_scale >= 4 and urine_color_scale < 6:
    print("Mild dehydration")
else:
    print("Severe dehydration")