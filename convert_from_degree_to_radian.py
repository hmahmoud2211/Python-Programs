# welcome message 
print ("Welcome to the program")
# welcome the user by his name 
name = input ("Enter your name : ").strip().title()
print ("Hello",name)
# insert the angle in rad
rad = eval (input("The angle in radian = "))
# change the rad to degree without rounding
import math
degree =(180/math.pi)* rad
# change the rad to degree with roundingeeq
degree_round = round((180/math.pi)* rad)
# print the statment and degree without rounding and degree with rounding 
print (name+",","you have entered",rad,"as aradian value, and it is",degree,"degrees without rounding and",degree_round,"degrees with rounding")