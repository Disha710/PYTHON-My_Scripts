d1= dict(
  place= "goa",
  code=560,
  city='panaji',
  distance= 123)

keys = d1.keys()
val = d1.values()
print(keys)
print(val)

print(list(keys))
print(list(val))

print(list(reversed(d1)))
print(list(reversed(d1.values())))
print(list(reversed(d1.items())))

print(d1)
print(d1['place'])
print(d1.get('code'))
print('goa' in d1)

d1["county"] = 'india'
print(d1)
d1.update(age = 20)
print(d1)

del d1["distance"]
print(d1)

sample = {'red': 'color', 'holi': 'celebration'}
for x, y in sample.items():
    print(x, y)
    
    
print('goa' in d1)
print('place' not in d1)


d2=sorted(d1)
print(d2)
print(sorted(d1.items()))
#print(sorted(d1,key=d1.get)) #mixed of int and str

#dic comprehension
d1_new = {x:'disha' for x in(2,4,5,6)}
print(d1_new)
