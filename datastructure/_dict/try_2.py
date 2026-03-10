d1= {
  'a':1,
  'b':2,
  'c':3,
  'd':6
}
print(d1)
print(d1['a'])
print(d1.get('x'))
d1['added']=40
k1=d1.keys()
v1=d1.values()
print('c' in d1)
print('c' not in d1)

for x, y in d1.items():
  print(x,y)
  
d1_comp = {x:x*2 for x in(2,4,5,6)}
print(d1_comp)
d1['z'] =4
print(d1)
print(list(k1))
print(list(v1))

del d1['a']


d1.update(a=5)
print(d1)
  
del d1["c"]


print(k1 & {"x","z","z","a"})
print(k1 | {"x","z","z","a"})
print(k1 ^ {"x","z","z","a"})