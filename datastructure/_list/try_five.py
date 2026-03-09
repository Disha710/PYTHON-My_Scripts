l1 = list(["me","you","hum"])
l1.append("he")
l1.extend(("his","her"))
l1.remove("hum")
print(l1.pop())
print(l1.index("you"))
l1.insert(2,"her")
del l1[2:]
print(l1[0])
print(l1)


