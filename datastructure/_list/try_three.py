l1 = list(("circle","triangle","oval","square"))
print(l1)

l2 = ["rabbit", "dog","cat","mouse"]
print(l2)

l1.append("triangle")
print(l1)

l1.extend(["shape","more"])

print(l1)

l2.insert(2,"added")

print(l2)

l2.remove("added")
print(l2)

print(l1.pop())
print(l1.pop(1))
print(l1)

del l1[1]
print(l1)

print(l1.count("oval"))
l1.reverse()
print(l1)

l1.sort(key=len)
print(l1)

#list as stack lifo
s1 = [1,2,3,4,5]
s1.append(6)
s1.append(7)
s1.pop()
print(s1)

#queue fifo
from collections import deque
q1 = deque(["x","y","z"])
print(q1)
q1.append("q")
print(q1)
q1.popleft()
print(q1)

#list comprehensive
v1= [-4,-5,0,-6,6,7,7]
sq = [x**2 for x in v1]
print(sq)
func = [abs(x) for x in v1 if x<-2] 
print(func)

t1= [(x,x*2) for x in v1]
print(t1)