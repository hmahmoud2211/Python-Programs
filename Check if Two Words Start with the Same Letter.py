# make the user enter the 2 words
word_1 = input("Enter the first word : ")
word_2 = input("Enter the second word : ")
# make a function that check the first letter of the given 2 words
def check(x,y):
    if x[0]==y[0] :
        return True
    else :
        return False
# print the return of the fuction 
print (check(word_1,word_2))