# welcome the student
print("Hello dear student,")
# Ask the student name
name = input("please enter your name : ").strip().title()
# Ask the student class
clas = input ("please enter your class : ").strip()
# Ask the student section 
section = input ("please enter your section : ").strip().title()
# Ask the subject name 
subject = input("please enter the subjuct name : ").strip().title()
# Ask the score of the subject
score = int (input("please enter your score in that subjuct : "))
# load the degree 
print ("-----Tracing your",subject,"mark-----")
# print the name of the student
print ("Name :",name)
# print the class
print ("Class:",clas)
# print the section 
print ("Section:",section)
# print the subject name with score
print (subject,"mark is",score)
#check if the degree between 0 to 100
if 0 < score < 100:
    # score below 50 fail
    if score < 50 :
        print ("unfortunately you fail in",subject)
    # score between 50 to 60 is good
    elif 50 <= score < 60 :
        print ("congratulation! pass in",subject)
        print ("Remark: good in",subject)
    # score between 60 to 80 is very good 
    elif 60 <= score < 80 : 
        print ("congratulation! pass in",subject)
        print ("Remark: very good in",subject)
   # score between 80 to 100 is outstanding 
    elif 80 <= score <= 100 : 
        print ("congratulation! pass in",subject)
        print ("Remark: outstanding in",subject)
# if the score is not between 0 to 100
else :
    print ("There is an eror because the score is not between 0 to 100")
# thank the student for using the program
print ("Thank you for using the program")