print ("insert the three numbers")
#the user will put the number
a,b,c = int(input("a = ")) , int(input("b = ")) , int(input("c = "))
#test a is bigger than b
if a > b :
    #test a is bigger than c
    if a > c :
        print (a,"is the biggest")
    else :
        print(c, "is the biggest ")
    #test b > c
elif b > c :
    print (b, "is the biggest")
else :
    print (c, "is the biggest")