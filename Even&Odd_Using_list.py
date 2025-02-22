# assign the orignal list
orignal_list = [2,5,6,8,10,9,11,12]
# make an empty list for even and odd 
even_list = []
odd_list = []
# print the orignal list 
print ("the orignal list:",orignal_list)
# make a loop to check if the numbers in the orignal list is even or odd
for i in orignal_list :
    x = i % 2
    # if the number is even add to even list
    # if the number is odd add to odd list
    if x == 0 :
        even_list.append(i)
    else :
        odd_list.append(i)
# print how many even numbers in the orignal list
print ("count of even numbers :",len(even_list))
# print how many odd numbers in the orignal list
print ("count of odd numbers :",len(odd_list))
# print the even list
print ("even list :",even_list)
# print the odd list
print ("odd list :", odd_list)