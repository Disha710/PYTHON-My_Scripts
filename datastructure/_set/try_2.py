s1 = {100,200,300,400,500}
s2 = {400,600,-8,-10,44,5}
print(s2)
print(s1)

print(len(s1))
print(15 in s1)
print(15 not in s2)

s2.update({4,6})
s2.add(-1)
s2.remove(5)
print(s2.pop())
print(s2)

print(s1&s2)
print(s1|s2)
print(s1^s2)