l1= [1,2,2,3,4,5]
l1.append(10)
l1.extend((12,24))
l1.insert(3,55)
l1.remove(3)
print(sorted(l1))
l1.pop(3)
del l1[3]
l1.sort(key = lambda x:x%2, reverse=False)
print(l1.index(1))
print(l1.index(2,1))
print(l1)

#fifo
from collections import deque
q1 = deque([1,2,3,4])
q1.append(0)
q1.popleft()
print(q1)

#list comprehensive
s1 =[3,4,5,6]
print([x/2 for x in s1])
print([(x,x*2,x+2) for x in s1])

print([(x,y) for x in range(6) for y in range(4)])


