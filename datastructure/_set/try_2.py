player = {"ravi","shahi","sam","muel","leo",'cat'}
print(player)

print('sam' in player)
print('Sam' in player)



print(len(player))
print(15 in player)
print(15 not in player)

player.update({4,6})
print(player)
player.add(-1)
print(player)
player.remove(-1)
print(player)
print(player.pop())
print(player)


s1 = set((100,200,300,400,500))
s2 = set((400,600,-8,-10,44,5))
print(s2)
print(s1)
print(s1-s2)
print(s1&s2)
print(s1|s2)
print(s1^s2)

#set comprehension
c = {x for x in player if isinstance(x,str)}
print(c)