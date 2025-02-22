# make a empty list 
l = []
# make a loop to insert a number in  the list 
while True :
    x = input("Enter a integer or enter done to quit : ") 
    if x == "done":
        break 
    else :
        num = eval (x)
        l.append(num)
# print this list
print (l)
# make the user enter the number that want to delete
y = int (input("enter the number you want to detele : "))
# remove evvery occurnce of this number from the list
for i in l :
    if i == y :
        l.remove(i)
# print the last edited list 
print (l)