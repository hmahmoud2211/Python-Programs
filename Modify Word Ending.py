# insert a word from the user 
word = input (" enter the word : ")
# get the last 3 letter of the word 
l3l= word[(len(word)-3):len(word)]
# check if the length of the word is bigger than three
# check if the last 3 leter is not ing then add to the word ing
if len(word) >= 3 and l3l != "ing":
    print (word+"ing")
# check if the last 3 letter is ing then add to the word ly 
elif l3l == "ing":
    print (word+"ly")
# check if the length of the word is less than 3 then print the word as it is 
elif len(word)< 3:
    print (word)