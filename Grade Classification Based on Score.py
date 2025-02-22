# enter your score 
x= int(input("Enter your score: "))
#check the score
if x>=90:
    #this gives excellent
    print ("A")
elif 80<=x<=89:
    #this gives very good 
    print ("B")
elif 70<=x<=79:
    #this gives good
    print ("c")
elif 60<=x<=69:
    #this gives pass
    print ("D")
else :
    #this gives failed
    print ("F")
