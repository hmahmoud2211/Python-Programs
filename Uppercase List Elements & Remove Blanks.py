# assign a list to 
l = []
#assign a second list to give the out put
l2 = []
# make a loop to make the user add the a list and assign in the first list
# add make the add charcter uppercase and add it to the second list
while True :
    x = input("Enter a integer or enter done to quit : ") 
    if x == "done":
        break 
    else :
        l.append(x)
        z = x.upper()
        l2.append(z)
# print the orignal list 
print (l)
# remove the empty sting is found 
for i in l2 :
    if i == "":
        l2.remove(i)
# print the edited list 
print (l2)