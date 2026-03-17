"""
Type of errors:
Logical
Syntax
Runtime error

Error handling methods are used for handling run time errors

Error handling key words:
blocks: try
        except
        finally
key words: raise
            assert

try:
    doubtful code
except:
    error handling code
finally:
    clean-up processing code

raise - To create custom errors
Assert - For debugging

The base class of all exception is Exception

Types of run time errors: Division by zero
                            Index out of range
                            File not found
                            Key error         These are predefined errors
"""

num1 = int(input("Enter number 1:"))    # 12
num2 = int(input("Enter number 2:"))    # 0

try:
    result = num1/num2                  # error
    print("Division result:",result)

except Exception as e:                  # catch error
    print(e)                            # printing error as division by zero

print("Completed..")                    # Completed..
print("File write...")                  # File write


lst = [12,45,21,78,34]

ind = int(input("Enter index:"))        # 10

try:
    print(lst[ind])                     # error

except Exception as e:
    print(e)                            # List index out of range

print("File writing....")               # File writing

