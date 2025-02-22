str1="CSCI29@#8496"
l1=[]
for i in str1:
    if i.isdigit() :
            l1.append(int(i))
print ("the sum of numbers in the string :",sum(l1))
print ("the averge of numbers in the string :",(sum(l1)/len(l1)))