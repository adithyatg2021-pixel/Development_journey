arun_fvt_color = ["red","green","yellow"]
hari_fvt_color = arun_fvt_color
krish_fvt_color = arun_fvt_color.copy() # shallow copy

hari_fvt_color[0] = "purple"

print("Arun fvt color:",arun_fvt_color)

print("Hari fvt color:",hari_fvt_color)

krish_fvt_color[0] = "white"

print("Krish fav color:",krish_fvt_color)

# is identity operator pointing to same memory or not

print(arun_fvt_color is hari_fvt_color)
print(arun_fvt_color is krish_fvt_color)