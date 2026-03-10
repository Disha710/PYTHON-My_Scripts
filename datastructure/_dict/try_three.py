d1= {
  'one': 1, 
  'two': 2, 
  'three': 3
  }

print(d1['one'])
print(d1.get('two'))
print('three' in d1)
d1["four"] = 4
d1.update(five =5)
d2=sorted(d1)
print(d2)
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