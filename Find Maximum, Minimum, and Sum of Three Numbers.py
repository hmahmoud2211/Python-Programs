# welcome the user and print the statment
print ("Hello sir, \nThe three numbers : ")
# insert the three numbers 
z,y,x = int(input("z = ")),int(input("y = ")),int(input("x = "))
# this is  the list 
l1 = [z , y, x]
# apply the variable to every element in the list 
a = l1[0]
b = l1[1]
c = l1[2]
# check if a > b
if a < b:
    # check if b < c then a min , c max , b in between
    if b < c:
        print ("The maximam number is",c)
        print ("The minimam number is",a)
        print (a, "<", b, "<", c)
        print ("["+str(a)+","+str(b)+","+str(c)+"]")
    # if not  b < c then a min , b max , c in between
    else:
        # check if a < c then a min , b max , c in between
        if a < c:
            print ("The maximam number is",b)
            print ("The minimam number is",a)
            print (a, "<", c, "<", b)
            print ("["+str(a)+","+str(c)+","+str(b)+"]")
        # if not  a < c then c min , b max , a in between
        else:
            print ("The maximam number is",b)
            print ("The minimam number is",c)
            print (c, "<", a, "<", b)
            print ("["+str(c)+","+str(a)+","+str(b)+"]")
# if not  a < b
else:
    # check if c < b then c min , a max , b in between
    if c < b:
        print ("The maximam number is",a)
        print ("The minimam number is",c)
        print (c, "<", b, "<", a)
        print ("["+str(c)+","+str(b)+","+str(a)+"]")
   # if not c < b
    else:
        # check if c < a then b min , a max , c in between
        if c < a:
            print ("The maximam number is",a)
            print ("The minimam number is",b)
            print (b, "<", c, "<", a)
            print ("["+str(b)+","+str(c)+","+str(a)+"]")
        #  if not  c < a then b min , c max , a in between
        else:
            print ("The maximam number is",c)
            print ("The minimam number is",b)
            print (b, "<", a, "<", c)
            print ("["+str(b)+","+str(a)+","+str(c)+"]")
# sum all the elements in the list 
s = a + b + c
# print the sum of the element 
print ("The sum of the three numbers = ",s)
# Thank the user 
print ("Thank you for using the program")