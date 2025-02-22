# welcome the student
print ("Hello dear student,")
# insert the number of classes attend
attend = int (input("please enter the number of classes attended : "))
# insert the number of classes held
held = int (input("please enter the number of classes held : "))
# to make percentage i need to know all the classes number
# the sum of classes number
s = attend + held
# to know the attendence percentege we divid the attendance number by the sum and multiply it with 100
per_attend = (attend/s)*100
# check if the percentage is greater than or equal 70% print you are allowed
if per_attend >= 70 :
    print ("your attendence percentage is",str(per_attend)+"% , you are allowed to take the exam")
# if the percentage is less than 70%  print you are not allowed
else :
    print ("your attendence percentage is",str(per_attend)+"% , you are not allowed to take the exam")
# thank the user
print ("Thank you for using the program")