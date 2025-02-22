# assign a loop 
l = [] 
#assign the cubic list 
cubic_list = []
# make a loop to make a user enter the nomber and assign it in the list 
while True :
    x = input("Enter a integer or enter done to quit : ") 
    if x == "done":
        break 
    else :
        num = eval (x)
        l.append(num)
print ("the orignal list :",l)
#make a loop to cube every number in the orignal list 
for i in l :
    x = i**3
    cubic_list.append(x)
# print the cubic list 
print ("the cubic value :",cubic_list)