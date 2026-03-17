string = input("Enter string:")

reverse = ""

string_length = len(string)

for i in range(string_length-1,-1,-1):
    reverse += string[i]
print("Reverse of string:",reverse)