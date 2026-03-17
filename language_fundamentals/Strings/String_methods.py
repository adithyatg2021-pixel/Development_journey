
"""
class str:

    def capitalize(): -> returns the word with first letter in uppercase
    
    def casefold(): -> returns the lowecase 

    def index(self,substr) -> returns the index of specified substring 

    def find(self,substr) -> returns the index of specified substring 

    def rfind(self,substr) -> returns the index of specified substring from right side

    def count(self,substr) -> return  number of time substring appears, it returns '0' if the substring
    is absent

    def isalpha() -> return true if string object is alphabet

    def isdigit() -> returns true if string object is digit

    def isalnum() -> returns true if string object is alphanumeric

    def startswith(self,prefix) -> returns True if the string starts with prefix

    def endswith(self,sufix) -> returns True if the string ends with sufix

    def strip(self) -> remove the space from both ends of the sring

    def lstrip(self) -> removes the white space or specified char from left

    def rstrip(self) -> removes the white space or specified char from right


"""

word = "luminarno TECHnolab" # word is an object of class 'str'
       #01234567890123456
# print(word.capitalize()) # Luminar technolab
# print(word.casefold())   # luminar technolab

"""
capitalize and casefold are the methods defined inside the class 'str', these methods can be call 
using the object 'word'.
"""
#------------------------------------------------------
#print(word.index("TECH")) # returns 8 as the starting index of TECH
#print(word.index("no"))   # returns the index of first occurennce of 'no'
#print(word.index("tech")) # returns error , python is case sensitive
#print(word.index("labs")) # returns error, 'labs' is not occuring in word

#-------------------------------------------------------------------------

# find() -> method used for returning the index of substring. 

"""
index() and find(), both are used to return the index of substring. find() will return a -1 if the
substring is not present.
"""

# print(word.find("labs")) # -1

# print(word.rfind("no"))  # 14

# print(word.count("no")) #2

#-----------------------------------------------------------------------------

# str1 = "hello"

# print(str1.isalpha()) # True , str1 is alphabet

# str2 = "hello124"

# print(str2.isalpha()) # False, str2 contain diigits

# num = "123"

# print(num.isdigit()) # True

# print(str2.isdigit()) # False

# print(str2.isalnum()) # True

# special = "hello12$"

# print(special.isalnum()) # False

#-------------------------------------------------------------------------------

# word1 = "luminar technolab"

# print(word1.startswith("lu")) # True

# print(word1.startswith("Lu")) # False

# print(word1.endswith("lab")) # True

# print(word1.endswith("labs")) # False

#--------------------------------------------------------------------------------

word2 = "   luminar technolab   "

print(word2)

print(f"left{word2.strip()}right")

word3 = "\nluminar"

print(word3)

print(word3.strip("\n"))

word4 = "\nluminar\t"

print(word4.lstrip("\nl")) #uminar
print(word4.rstrip("r\t")) #lumina