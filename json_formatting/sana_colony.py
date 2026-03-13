import json
sana_colony = { 
  "family" : {  
      "fam1": {
      "father" : "jon",
      "Mother" : "sari",
      "kids":[
        {
          "name": "malti",
         "age" : 25
        },
        { "name": "don",
         "age"  : 33
         } 
      ]  
    },
    "fam2": {
      "father" : "papa",
      "Mother" : "mama",
      "kids":[
        {
          "name": "son1",
         "age" : 2
        },
        { "name": "son2",
         "age"  : 10
         } 
      ] 
      
    },
    "fam3" :{
      "father" : "sana",
      "Mother" : "sunny",
      "kids":[
        {
          "name": "santoor",
         "age" : 10
        },
        { "name": "sima",
         "age"  : 15
         } 
      ] 
    }  
  }  
}


print(list(sana_colony.keys()))
print("family" in sana_colony) 
print([kid["name"] for kid in sana_colony["family"]["fam1"]["kids"]])  # kids of fam1

with open('sana_colony.json', mode = 'w',encoding='utf-8') as f:
  json.dump(sana_colony,f,indent = 2)
  
with open('sana_colony.json', mode = 'r',encoding='utf-8') as f:
  data = json.load(f)
  
print(json.dumps(data, indent=2))