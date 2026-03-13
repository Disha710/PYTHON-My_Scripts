s1 =set([0,1,2,3,5,8,13]) #single iterable argument
s2 = {0,1,2,3,5,8,13}
print(s2)
print(s1)

print(len(s1))
print(15 in s1)
print(s1)
print(15 not in s2)


s2.update({4,6})
print(s1)
s2.add(-1)
print(s1)
s2.remove(5)
print(s1)
print(s2.pop())
print(s1)

print(s1-s2)
print(s1&s2)
print(s1|s2)
print(s1^s2)

#set comprehension
c = {x**2 for x in range(1, 6)}
d = {x**2 for x in s1}
print(c,d)