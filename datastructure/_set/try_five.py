colour = {"pink","yellow","orange"}

print(colour)

print('pink' in colour)


print('pinl' not in colour)
colour.update(("black",'brown','greenish'))
colour.add("last_color")
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