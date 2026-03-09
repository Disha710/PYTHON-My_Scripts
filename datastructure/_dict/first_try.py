dishes = {
  "eggs":2, 
  "suasage":1,
  "bacon":2,
  "spam": 500
}

keys = dishes.keys()
val = dishes.values()
print(keys)
print(val)
n = 0
for x in val:
  n+= x
  
print(n)

print(list(keys))
print(list(val))

del dishes["spam"]

print(list(keys))

print(keys & {"eggs","bacon","juice"})
print(keys | {"eggs","bacon","juice"})
print(keys ^ {"eggs","bacon","juice"})

print(list(reversed(dishes)))
print(list(reversed(dishes.values())))
print(list(reversed(dishes.items())))
dishes.update(salad=7)
print(dishes)

sorted(dishes)
print(dishes)

print('salad' in dishes)
print('salad' not in dishes)

dishes["bacon"]= 9
print(dishes)