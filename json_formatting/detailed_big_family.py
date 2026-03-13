import json
family_data = {
  "father" : "rahul",
  "Mother" : "simran",
  "kids" :[
    {
      "name" :"rose",
      "age" : 10
    },
    {
      "name" :"lili",
      "age" : 12
    },
    {
      "name" : "bud",
      "age"  : 15
    }
  ]
}
print(list(family_data.keys()))
print("kids" in family_data) 
for kid in family_data["kids"]:
  print(kid["name"])          

with open('detailed_big_family.json', mode = 'w',encoding='utf-8') as f:
  json.dump(family_data,f,indent = 2)
  
with open('detailed_big_family.json', mode = 'r',encoding='utf-8') as f:
  data = json.load(f)
  
print(json.dumps(data, indent=2))