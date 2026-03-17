
string = input("Enter string:")

new_str = ""

# rev = string[::-1]

for i in range(len(string)-1,-1,-1):
    new_str += string[i]

if string == new_str:
    print(string,"is palindrome")
else:
    print(string,"is not palindrome")