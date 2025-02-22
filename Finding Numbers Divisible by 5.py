# assign a list 
l = [] 
# assign for the list will have the no that is divisibale by 5
l2 = []
# make a loop to make a user enter the nomber and assign it in the list 
while True :
    x = input("Enter a integer or enter done to quit : ") 
    if x == "done":
        break 
    else :
        num = eval (x)
        l.append(num)
for i in l :
    if i%5 == 0:
        l2.append(i)
print ("the divisible by 5 :",l2)