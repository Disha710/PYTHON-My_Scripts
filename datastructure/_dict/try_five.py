d1= dict(
  place= "goa",
  code=560,
  city='panaji',
  distance= 123)

print(d1)
print(d1['place'])
print(d1.get('code'))
print('goa' in d1)
d1["county"] = 'india'
d1.update(age = 20)
d2=sorted(d1)
print(d2)
print(d1)

sample = {'red': 'color', 'holi': 'clebration'}
for x, y in sample.items():
    print(x, y)