import json

family_data = {
  "father" : "Tom",
  "Mother" : "Ellna",
  "Kids" : "Jan"
  
}
print(family_data["father"])

with open('small_family.json', mode='w', encoding='utf-8') as f:
  json.dump(family_data, f, indent=2)
  
with open('small_family.json', mode='r', encoding='utf-8') as f:
  data_1 = json.load(f)
print(json.dumps(data_1, indent=0))
  
print(family_data)