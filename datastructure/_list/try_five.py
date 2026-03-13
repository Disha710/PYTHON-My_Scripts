lang = ['konkani', 'Marathi','English','Hindi','Hindi']
print(lang.count('Hindi'))
print(lang.count('me'))
print(lang.index('Hindi',-1))
lang.reverse()
print(lang)
lang.append('Deutsch')
print(lang)
lang.sort()
print(lang)
lang.sort(reverse = True)
print(lang)
print(lang.pop())
lang.insert(-1,"Tamil")
print(lang)
print(lang.pop(0))

num = [2,4,16,32,64]
num.insert(0,0)
num.extend([124,247,1246])
print(num)
print(num.pop())
print(num)

from collections import deque
queue = deque(['riya','siya','kia'])
queue.append('mia')
queue.append('mia2')
print(queue)
queue.popleft()
queue.popleft()
print(queue)

add = list(map(lambda x,y:x+y,range(3),range(4)))
print(f'addition of number is {add}')

#list comprehensive
vector = [-4105,0,32,-67]
print([x*2 for x in vector])



filter_list1 = [x for x in lang if len(x)>5]
filter_list2 = [x for x in lang if x[0]=='H']
print(filter_list1)
print(filter_list2)

abs_1= [abs(x) for x in vector]

t1 = [
  (x,x//2) for x in range(6)
]
print(t1)


del vector[2:4]
print(vector)



x, *y, z = lang
print(x)
