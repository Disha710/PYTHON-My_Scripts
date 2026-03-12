d1= {
  'one': 1, 
  'two': 2, 
  'three': 3
  }
print(d1.keys())
print(d1.values())
print(list(d1.keys()))
print(list(d1.values()))
print(d1['one'])
print(d1.get('two'))
print('three' in d1)
d1["four"] = 4
d1.update(five =5)

print(d1)

text = {'my name': 'Hero', 'Disha': 'the brave'}
for k, v in text.items():
    print(k, v)
    
k1= d1.keys()
v2 = d1.values()

print(k1,v2)

print(k1 | {0,1,2,3,5,8,13})
print(k1 & {0,1,2,3,5,8,13})
print(k1 ^ {0,1,2,3,5,8,13})

print(list(reversed(d1)))
print(list(reversed(d1.values())))
print(list(reversed(d1.items())))
d1.update(updated = 0)
print(d1)
d1["lastkeys"]= 100
print(d1)

print(90 in d1)
print('unkown' not in d1)

del d1['three']
print(d1)

# sort will not work on dictionary only sorted()
print(sorted(d1)) #sort d1.keys()
print(sorted(d1,key=d1.get)) #sort by values
print(sorted(d1.items()))

#list comprehension
d2 = {x:x.lower() for x in text}
print(d2)