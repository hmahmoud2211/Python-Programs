print ("input the three angle")
# insert the three side 
a,b,c  = int(input("a = ")),int(input("b = ")),int(input("c = "))
# sum of angles
s = a+b+c
# condition
if s==180 :
    print("valid")
else:
    print ("invalid")