# welcome the student
print ("Hello sir,")
# insert the number of rows
row = int(input("please enter the number of rows : "))
# print the statment of requre 
print ("Right angle triangle with stares : ")
# make a loop to make the numbers of rows in the triangle
for i in range (1,row +1 ):
    for j in range (i):
        print (i * i, end = " ")
    print (" ")