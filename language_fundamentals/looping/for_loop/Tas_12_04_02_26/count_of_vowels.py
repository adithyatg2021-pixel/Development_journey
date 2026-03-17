string = input("Enter string:")

VOWELS = "aeiou"

count = 0

for i in string:
    if i in VOWELS:
        count += 1
print("Count of vowels in",string,":",count)