def fibanocci(num):
    f1 = 0
    f2 = 1
    print(f1)
    print(f2)
    next = 0
    while(next < num):
        next = f1 + f2
        print(next)
        f1 = f2
        f2 = next
         
fibanocci(10)

