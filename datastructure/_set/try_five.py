colour = {"pink","yellow","orange"}

print(colour)

print('pink' in colour)
print('pink' not in colour)

print(len(colour))
colour.update(("black",'brown','greenish'))
print(colour)
colour.add("last_color")
colour.remove('pink')
print(colour)
print(colour.pop())
print(colour)

print(colour)
for x in colour:
  print(x)
print(colour)

a = set([1,2,3,4])
b = set([3,4,5,6,7])

print(a)
print(b)

print(a-b) 
print(a & b) 

print(a | b)  

print(a^b) 

#set comprehension
c = {x for x in colour if len(x)>4 and isinstance(x, str) }
print(c)