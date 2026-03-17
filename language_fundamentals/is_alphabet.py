char = input("Enter character:")

# ascci_value = ord(char)

# if ascci_value in range(97,123) or ascci_value in range(65,91):
#     print("Alphabet")
# else:
#     print("Not alphabet")

#or

if "a" <= char <= "z" or "A" <= char <= "Z":
    print("Alphabet")
else:
    print("Not alphabet")