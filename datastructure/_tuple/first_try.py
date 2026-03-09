t1 = 12345, 54671, 'hello!'
print(t1[0])
print(t1)
print(t1)
u = t1,(1,2,3,4,5)
print(u)

v = ([1,2,3,4,5],["x","y"])
v[1].append("z")
v[0].pop(1)

print(v)

#unpacking

x, *y,z=t1
print(y)