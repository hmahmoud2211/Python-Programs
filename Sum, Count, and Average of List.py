# assign a loop 
l = [] 
# make a loop to make a user enter the nomber and assign it in the list 
while True :
    x = input("Enter a integer or enter done to quit : ") 
    if x == "done":
        break 
    else :
        num = eval (x)
        l.append(num)
# assign the sum of the list to a veriable 
y = sum (l)
# assign the length of the list to a veriable 
z = len (l)     
# print the sum and count and averge    
print ("total sum :",y)
print ("count of entered numbers : ",z)
print ("averege of the numbers :",y/z)