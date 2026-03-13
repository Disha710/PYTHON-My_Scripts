fruits = ['orange', 'banana','apple','kiwi','papaya','apple']
print(fruits.count('apple'))
print(fruits.count('me'))
print(fruits.index('apple',2))
fruits.reverse()
print(fruits)
fruits.append('pineapple')
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
print(fruits.pop())
fruits.insert(0,"me")
print(fruits)
print(fruits.pop(0))

stack = [1,2,5,6]
stack.extend([1,2,3])
print(stack)
print(stack.pop())
print(stack)

from collections import deque
queue = deque(['si','be','re'])
queue.append('came1')
queue.append('came2')
print(queue)
queue.popleft()
queue.popleft()
print(queue)

square = list(map(lambda x:x**2,range(10)))
print(square)


vector = [-4,-5,0,2]
new1 = [x*2 for x in vector]
print(new1)

list1 = [-5,-6,0,4,5,6,-7]
filter_list1 = [x for x in list1 if x>=0]
print(filter_list1)

f1 = [abs(x) for x in vector]

tuple_2 = [
  (x,x**2) for x in range(6)
]
print(tuple_2)

a= ["dfg",66.5,77.8,3,0,1]
del a[2:4]
print (a)


x, *y, z = fruits
print(x)
