# put the original list
l = [2,5,6,8,10,9,11,12]
# define empty even list to put even no 
even_list = []
# define empty odd list to put odd no
odd_list = []
#make a loop to get to every no in the list and check if the no is even or odd
for i in l :
    x = i%2 
    if x == 0:
        # assign the even no in the even list
        even_list.append(i)
    else :
        #assign the odd no in the odd list 
        odd_list.append(i)
# print the orignal list 
print("the orignal list :",l)
# print the count of even and odd no
print ("count the even number :",len(even_list))
print ("count the odd number :",len(odd_list))
# print the even and odd list 
print ("the even list :",even_list)
print ("the odd list :",odd_list)