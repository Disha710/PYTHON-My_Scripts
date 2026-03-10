place = {"goa","kerala","TN","AP","Bihar"}

print(place)

print('bihar' in place)


a= set(("x","y","z",4,-4,0))
b = set(("ABC",0,None,4,6,True, False ))

print(a)
print(b)

print(a-b) 
print(b-a) 
print(a | b) 

print(a & b)  

print(a^b) 

c = {x for x in a if isinstance(x,(int,float))}
print(c)