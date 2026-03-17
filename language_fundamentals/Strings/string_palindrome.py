word = input("Enter string:")

word_length = len(word) - 1

result = "" 

for i in range(word_length,-1,-1):
    result += word[i]
print("Palindrome" if result == word else "Not palindrome")