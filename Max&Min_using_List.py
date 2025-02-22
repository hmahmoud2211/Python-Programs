# assign a empty list
l=[]
# make a loop to let the user enter a number and add it to list
while True:
    x = input ("enter the number : ")
    if x == "done":
        break
    else :
        num = int(x)
        l.append(num)
# print the maximam number in list
print ("the maximam number :",max(l))
# print the minimam number in list
print ("the minumum number :",min(l))