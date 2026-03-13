import json
family_data = {
  "father" : "Pappa",
  "Mother" : "Mom",
  "kids" : {
    "name" : "son",
    "age" : 10
  }
  
}
print(family_data.keys())
print(family_data["kids"]["name"])

with open('detailed_small_family.json', mode = 'w',encoding='utf-8') as f:
  json.dump(family_data,f,indent = 2)
  
with open('detailed_small_family.json', mode = 'r',encoding='utf-8') as f:
  data = json.load(f)
  
print(json.dumps(data, indent=2))