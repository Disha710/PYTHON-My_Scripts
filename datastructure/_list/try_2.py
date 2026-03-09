l1 = [-44,3500, -1,0,5,6,7,8]
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

l2 = [x**2 for x in l1]
print(l2)

ori = list(map(lambda x:x//10, l2[:]))
print(ori)

l3= [x for x in l2 if x>10]
print(l3)

del l3