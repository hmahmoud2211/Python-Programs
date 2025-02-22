print ("input the three side")
# insert the three side 
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
#check if the side vaid for triangle 
if (a+b)>c :
    if (b+c)>a:
        if (a+c)>b:
            # s is the half of the perimeter 
            s = (a+b+c)/2
            # calculate the area
            import math
            A = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print(A)
else :
    print("this side is invalid for a triangle") 