
def calculator(n1,n2,op="+"):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    
print("Result is",calculator(10,5,"*"))
print("Result is",calculator(10,5))