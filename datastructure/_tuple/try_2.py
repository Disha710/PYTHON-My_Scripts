t1 = 'paper', 'wood', 'ash',450
print(t1)
print(t1[0])
print(t1)
t2 = t1,(1,2,3,4,5)
print(t2)

v = ([1,2,3,4,5],["x","y"])
v[1].append("z")
v[0].pop(1)

print(v)

#unpacking

x, *y = t1
print(y)