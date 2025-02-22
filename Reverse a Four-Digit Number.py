# welcome the user
print ("Hello sir,")
# insert the 4 digit no
num = int(input("please enter 4 digit numbers : "))
# the reversed number at the beggin is 0
rev_num = 0
## check if the number is 4 digit 
if 999 < num < 10000:
    # make a loop to reverse the number 
    while num != 0 :
        # get the last digit of the number
        last_dig = num % 10
        # to get the place value of the 4 digit 
        rev_num = rev_num * 10
        # add the the last number to the reverserd number
        rev_num = rev_num + last_dig
        # delete the last digit from the main number
        num = num // 10
    # print the reverse number
    print("The reverse number is",rev_num)
else :
    print ("there is an eror because the number must be 4 digit number")