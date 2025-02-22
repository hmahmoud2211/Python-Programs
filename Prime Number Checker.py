# make the user enter the number
x = eval (input("enter the number you want to check :"))
# the 2,3,5 is the main numbers to  divide to check the number is prime or not
p1 ,p2 ,p3=2 , 3, 5
# assign the reminder to a variables 
z,c,a = x%p1 , x%p2 , x%p3
# check if the number equal 2,3,5
if x==p1 or x==p2 or x==p3 :
    print ("this number is prime :",x )
else:
    # if the reminder equal 0 then the number is not prime and vice versa
    if z!=0 or c!=0 or a!=0 :
        print ("this number is not prime :",x)
    else :
        print ("this number is prime :",x)