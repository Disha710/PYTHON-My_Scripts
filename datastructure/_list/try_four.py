l1 = ["rabbit", "dog","cat","mouse"]
print(l1.count('rabbit'))
print(l1.count('DOG'))
print(l1.index("mouse",2))
l1.reverse()
print(l1)
l1.append('added')
l1.insert(2,"my_pet")
print(l1)
l1.remove("added")
print(l1)
l1.extend((12,24))
l1.insert(3,"extra")
print(l1)
l1.remove(24)
l1.pop()
#print(sorted(l1))
l1.pop(3)
del l1[3]
print(l1)
l1.sort(key = lambda x:x[0], reverse=False)
print(l1.index("rabbit"))
print(l1.index('rabbit',1))
print(l1)


#stack lifo
v1 = [3,9,12,15]
v1.extend([0,1,6])
print(v1)
print(v1.pop())
print(v1)

#fifo
from collections import deque
q1 = deque([1,2,3,4])
q1.append(0)
q1.popleft()
print(q1)

#list comprehensive
s1 =[3,4,5,6]
print([x/2 for x in s1])

#tuple
print([(x,x*2,x+2) for x in s1])

print([(x,y) for x in range(6) for y in range(4)])

*x, z = l1
print(x)
