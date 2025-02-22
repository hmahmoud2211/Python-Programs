# let the user enter the word 
word = input ("enter the word : ")
# remove the space from the sentence 
rem_space = word.replace(" ","")
# print the count of the word without the space 
print("output :",len(rem_space))