# welcome by the user 
print("Hello Sir,")
# enter the price 
price = int(input ("please enter your quantity : "))
# check if the quantity is bigger than or equal 1200
if price >= 1200 :
    # calculate the discount
    dis = price - (price*0.1)
    print ("the final price after discount is",dis)
# if the quantity is not bigger than or equal 1200 print no discount
else :
    print ("unfortunately there is no discount because the price is less than 1200")
# thank the user for using the program
print ("thank you for using the program")