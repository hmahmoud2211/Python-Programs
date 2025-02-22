d = {}
string = input ("enter you string : ").lower()
for i in string:
    d[i]= string.count(i)
print (d)
