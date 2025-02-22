# assign the first list
l1 = []
# assign the seccond list
l2 = []
# make a loop to add a number in the first list 
while True :
    x = input("Enter a integer in the first list or enter done to quit : ") 
    if x == "done":
        break 
    else :
        num = eval (x)
        l1.append(num)
# make a loop to add a number in the second list 
while True :
    y = input("Enter a integer in the second list or enter done to quit : ") 
    if y == "done":
        break 
    else :
        num1 = eval (y)
        l2.append(num1)
# get the index of the last number in the fist and second list 
z = len(l1) - 1
c = len(l2) - 1
# assign the first no and second no to of every list to variable 
fl1 = l1[0]
ll1 = l1[z]
fl2  = l2[0]
ll2 = l2[c]
# It prints True if the first number of list1 and the last number of list2 are the same.
# It also prints True if the first number of list2 and the last number of list1 are the same.
# Otherwise, it prints false 
if fl1 == ll2 or fl2 == ll1 :
    print ("true")
else :
    print ("false")
