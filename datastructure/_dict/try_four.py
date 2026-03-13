animal = {
  "dog":2, 
  "cat":1,
  "pig":2,
  "dove": 500
}

keys = animal.keys()
val =   animal.values()
print(keys)
print(val)

print(list(keys))
print(list(val))

print(animal["dog"])
animal['extra'] =5
animal.update(update=80)
animal.pop("extra")
print(animal)
  

print(list(keys))
print(list(val))

del animal["pig"]


print(keys & {"aimal","cat","pigeon"})
print(keys | {"aimal","cat","pigeon"})
print(keys ^ {"aimal","cat","pigeon"})

print(list(reversed(animal)))
print(list(reversed(animal.values())))
print(list(reversed(animal.items())))


animal.update(cow=7)
print(animal)



print('cat' in animal)
print('cat' not in animal)

#sorting
print(sorted(animal))
print(sorted(animal.items()))
print(sorted(animal, key = animal.get))

#list comprehension
d1_comp = {x:animal[x] for x in animal}
print(d1_comp)
