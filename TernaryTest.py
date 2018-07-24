try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    c=int(input("Enter third number"))
    '''This is two number only'''
    #min=a if a<b else b

    '''This is for 3 numbers'''
    min=a if a<b and a<c else b if b<c else c
    print("Minimum value",min)
except Exception:
    print("OOPS.......!!!! Enter valid number")



