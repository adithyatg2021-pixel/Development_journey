
lst = [12,45,21,78,34]

ind = int(input("Enter index:"))    # 6       

try:
    print(lst[ind])                 # Error 

except Exception as e:
    print(e)                        # List index out of range

    ind = int(input("Enter index:")) # 10

    try:
        print(lst[ind])              # Error
    
    except Exception:
        ind = int(input("Enter index:")) # 12

finally:      
    print("File writing....")           # File writing....
    print("Db commit....")              # Db commit.....

# It is not possible to resolve the error inside finally block


