place = {"goa","kerala","TN","AP","Bihar"}

print(place)

print('goa' in place)


print('goa' not in place)

print(len(place))
place.update((0,'MP'))
print(place)
place.add('up')
print(place)
place.remove(0)
print(place)
print(place.pop())
print(place)



a= set(("x","y","z",4,-4,0))
b = set(("ABC",0,None,4,6,True, False ))

print(a)
print(b)

print(a-b) 
print(b-a) 
print(a | b) 

print(a & b)  

print(a^b) 

#set comprehension
c = {x for x in a if isinstance(x,(int,float))}
print(c)