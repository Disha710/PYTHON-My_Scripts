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

animal.update(salad=7)
print(animal)



print('cat' in animal)
print('cat' not in animal)

