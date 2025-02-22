z,y = eval(input("z = ")),eval(input("y = "))
if type(z) == int and type(y) == int:
    if z>y :
        print ("the maximam number is",z)
    else : 
        if z<y :
            print ("the maximam number is",y)
        else :
            if z==y :
                print("The two numbers are equal")
else :
    print ("Enter intger number only")
