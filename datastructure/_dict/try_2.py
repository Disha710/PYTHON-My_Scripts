d1= {
  'a':1,
  'b':2,
  'c':3,
}
k1=d1.keys()
v1=d1.values()

for x, y in d1.items():
   y+=1
print(y)
d1['z'] =4
print(d1)
print(list(k1))
print(list(v1))

del d1['a']


d1.update(a=5)
print(d1)
  