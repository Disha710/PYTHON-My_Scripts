import json

family_data = {
  "Father" : "raghul",
  "Mother" : "Diana Pinto",
  "kids" : ["nath","gokulnath","manjunath"]
  
  
}

with open('big_family.json',mode='w',encoding = "utf-8") as f:
  json.dump(family_data,f,indent = 4)
  
with open('big_family.json',mode='r',encoding = "utf-8") as f:
  data = json.load(f)
  
print(json.dumps(data, indent=2))

print(family_data["kids"])
  
  