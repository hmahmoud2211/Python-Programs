# welcome the user
print ("Hello sir,")
# insert the number of multipcation table 
num = int (input("please enter the number of multiplaction table : "))
# print the statment of require 
print ("The multiplaction table of",num,":")
# make a walet to save the number of multiplied number in it
s = 0
# make a while loop to calculate the multiplication 
# make the multiplication till 12
while s <= 11:
    # add to the wallet one to print it at the first time *1
    s = s + 1
    # make the operation
    result = num * s
    # print the number multiply with the number in the walet equal the result
    print (num,"x",s,"=",result) 
# thank the user 
print ("Thank you for using the program")