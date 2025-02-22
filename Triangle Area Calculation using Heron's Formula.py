print ("input the three side")
# insert the three side 
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
# s is the half of the perimeter 
s = (a+b+c)/2
# calculate the area
import math
A = math.sqrt(s*(s-a)*(s-b)*(s-c))
print (A)