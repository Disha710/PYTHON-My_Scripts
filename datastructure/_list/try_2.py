l1 = [-44,5,3500, -1,0,5,6,7,8]
print(l1.count(0))
print(l1.count(None))
print(l1.count('Disha'))
print(l1.index(5,2))
l1.reverse()
print(l1)
l1.append(90)
l1.extend(["Numbers"])
print(l1)
l1.insert(4,"insert")
print(l1)
l1.remove("insert")
print(l1)
print(l1.pop())

print(l1.index(0)) #0 at index 3

print(l1.count(0))

l1.sort(key = None, reverse=False)
print(l1)

from collections import deque
queue = deque(l1)
queue.append(6)
queue.append(100)
print(f"queue is : {queue}")
queue.popleft()
queue.popleft()
print(queue)

#map(function,iterable)
ori = list(map(lambda x:x//10, l1))
print(ori)

#list comprehensive
l2 = [x**2 for x in l1]
print(l2)

x=[abs(x) for x in l1]
print(f'positive value {x}')

l3= [x for x in l2 if x>10]
print(l3)

#creating tuple
tuple_1 = [
  (x,x+1,1) for x in range(2,10)
  ]
print(f"Tuple is : {tuple_1}")

#delete
del l3[3:5]
print(l3)

#unzipping
x,*z = l3
print(x)
print(z)