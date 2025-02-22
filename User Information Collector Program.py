# ask user for his name , age and siblings 
name = input("what is your name? ")
age = input("what is your age? ")
siblings = input("how many siblings do you have? ")
motherName = input("What is your mother’s name? ")
#remove extra space and capital
name=name.strip().title()
age=age.strip()
siblings=siblings.strip()
motherName=motherName.strip().title()
# say hello for user and info for his age and no of sib 
print("hello,",name)
print("your age is ",age)
print("you have",siblings,"siblings")
print("your mother’s name is", motherName)
